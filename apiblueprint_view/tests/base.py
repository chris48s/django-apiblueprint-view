from bs4 import BeautifulSoup
from django.test import TestCase, RequestFactory
from apiblueprint_view.views import ApiBlueprintView


class ApibpTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def get_response(self, fixture):
        view = ApiBlueprintView.as_view(blueprint=fixture)
        response = view(self.factory.get('/foo/bar'))
        response.render()
        return response

    def get_html(self, response):
        return response.content.decode('utf-8')

    def assertInIgnoreFormatting(self, needle, haystack):
        # use bs4 to standardise the formatting of both chunks of html
        needle_formatted = BeautifulSoup(needle, "html.parser").prettify()
        haystack_formatted = BeautifulSoup(haystack, "html.parser").prettify()

        # then strip the leading/trailing whitespace when we
        # compare to account for indentation differences
        self.assertIn(
            "\n".join([x.strip() for x in needle_formatted.split("\n")]),
            "\n".join([x.strip() for x in haystack_formatted.split("\n")]),
        )

    def assertNotInIgnoreFormatting(self, needle, haystack):
        # use bs4 to standardise the formatting of both chunks of html
        needle_formatted = BeautifulSoup(needle, "html.parser").prettify()
        haystack_formatted = BeautifulSoup(haystack, "html.parser").prettify()

        # then strip the leading/trailing whitespace when we
        # compare to account for indentation differences
        self.assertNotIn(
            "\n".join([x.strip() for x in needle_formatted.split("\n")]),
            "\n".join([x.strip() for x in haystack_formatted.split("\n")]),
        )
