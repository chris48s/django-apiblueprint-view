import copy
import os
import re

import markdown2
from django.conf import settings
from django.core.exceptions import SuspiciousFileOperation
from django.utils._os import safe_join

from . import dm


class ApibpParser:
    """
    Draughtsman can handle most of the heavy lifting for us
    but we need to do a bit of additional processing on
    the parsed data structure to make it easier to render
    """

    def __init__(self, blueprint):
        self.blueprint = os.path.abspath(blueprint)
        self.api = None
        self.host = None
        self.process_includes = getattr(settings, "APIBP_PROCESS_INCLUDES", True)
        self.include_whitelist = getattr(
            settings, "APIBP_INCLUDE_WHITELIST", [".md", ".apibp", ".json"]
        )

    def _set_host(self):
        for element in self.api.content[0].attributes["meta"]:
            if element.key.content == "HOST":
                self.host = element.value.content

    def _make_example(self, element):
        if element.attributes["href"].content:
            element.attributes["hrefExample"] = copy.copy(element.attributes["href"])
        if self.host:
            element.attributes["hrefExample"].content = (
                self.host + element.attributes["hrefExample"].content
            )
        if "hrefVariables" in element.attributes:
            replacements = {
                var.key.content: var.value.content
                for var in element.attributes["hrefVariables"].content
            }
            try:
                element.attributes["hrefExample"].content = element.attributes[
                    "hrefExample"
                ].content.format(**replacements)
            except KeyError:
                pass

    def _propogate_hrefs(self, element):
        for transition in element.transitions:
            for transaction in transition.transactions:
                transaction.request.attributes["href"] = element.attributes["href"]

    def _parse_markdown(self, element):
        element.content = markdown2.markdown(element.content)

    def _is_whitelisted(self, filename):
        return True in [filename.endswith(ext) for ext in self.include_whitelist]

    def _replace_includes(self, apibp):
        matches = re.findall(r"<!-- include\((.*)\) -->", apibp)
        for match in matches:
            include_path = safe_join(os.path.dirname(self.blueprint), match)

            if not self._is_whitelisted(include_path):
                raise SuspiciousFileOperation("extension not in whitelist")

            # recursively replace any includes in child files
            with open(include_path, "r") as f:
                include_apibp = self._replace_includes(f.read())

            apibp = apibp.replace("<!-- include(" + match + ") -->", include_apibp)

        return apibp

    def _post_process(self, root):
        for element in root:
            if hasattr(element, "element"):
                if element.element == "copy":
                    self._parse_markdown(element)
                if element.element == "resource":
                    self._make_example(element)
                    self._propogate_hrefs(element)
                    if "hrefVariables" in element.attributes:
                        for param in element.attributes["hrefVariables"].content:
                            if hasattr(param, "description"):
                                try:
                                    self._parse_markdown(param.description)
                                except AttributeError:
                                    pass
                try:
                    self._post_process(element.content)
                except TypeError:
                    pass

    def parse(self):
        with open(self.blueprint, "r") as f:
            apibp = f.read()
        if self.process_includes:
            apibp = self._replace_includes(apibp)
        self.api = dm.parse(apibp)
        self._set_host()
        self._post_process(self.api[0])

        return self.api
