import copy
import markdown2
import os
import re
from draughtsman import parse


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

    def _set_host(self):
        for element in self.api.content[0].attributes['meta']:
            if element.key.content == 'HOST':
                self.host = element.value.content

    def _make_example(self, element):
        if element.attributes['href'].content:
            element.attributes['hrefExample'] =\
            copy.copy(element.attributes['href'])
        if self.host:
            element.attributes['hrefExample'].content =\
            self.host + element.attributes['hrefExample'].content
        if 'hrefVariables' in element.attributes:
            replacements = {
                var.key.content: var.value.content for\
                var in element.attributes['hrefVariables'].content
            }
            try:
                element.attributes['hrefExample'].content =\
                element.attributes['hrefExample'].content.format(
                    **replacements)
            except KeyError:
                pass

    def _propogate_hrefs(self, element):
        for transition in element.transitions:
            for transaction in transition.transactions:
                transaction.request.attributes['href'] =\
                element.attributes['href']

    def _parse_markdown(self, element):
        element.content = markdown2.markdown(element.content)

    def _replace_includes(self, apibp):
        matches = re.findall(r'<!-- include\((.*)\) -->', apibp)
        for match in matches:
            include_path = os.path.join(os.path.dirname(self.blueprint), match)

            # recursively replace any includes in child files
            include_apibp = self._replace_includes(
                open(include_path, 'r').read())

            apibp = apibp.replace(
                '<!-- include(' + match + ') -->', include_apibp)

        return apibp

    def _post_process(self, root):
        for element in root:
            if hasattr(element, 'element'):
                if element.element == 'copy':
                    self._parse_markdown(element)
                if element.element == 'resource':
                    self._make_example(element)
                    self._propogate_hrefs(element)
                    if 'hrefVariables' in element.attributes:
                        for param in element.attributes['hrefVariables'].content:
                            if hasattr(param, 'description'):
                                self._parse_markdown(param.description)
                try:
                    self._post_process(element.content)
                except TypeError:
                    pass

    def parse(self):
        apibp = self._replace_includes(open(self.blueprint, 'r').read())
        self.api = parse(apibp)
        self._set_host()
        self._post_process(self.api[0])

        return self.api
