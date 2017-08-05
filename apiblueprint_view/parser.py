import copy
import markdown2
import os
from draughtsman import parse


class ApibpParser:
    """
    Draughtsman can handle most of the heavy lifting for us
    but we need to do a bit of additional processing on
    the parsed data structure to make it easier to render
    """

    def __init__(self, blueprint):
        self.blueprint = blueprint
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

    def _post_process(self, root):
        for element in root:
            if hasattr(element, 'element'):
                if element.element == 'copy':
                    self._parse_markdown(element)
                if element.element == 'resource':
                    self._make_example(element)
                    self._propogate_hrefs(element)
                try:
                    self._post_process(element.content)
                except TypeError:
                    pass

    def parse(self):
        self.api = parse(open(os.path.abspath(self.blueprint), 'r').read())

        self._set_host()
        self._post_process(self.api[0])

        return self.api
