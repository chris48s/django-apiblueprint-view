from .base import ApibpTest


h2 = """
<h2 id="quick-start-2">
  Quick start
  <a class="permalink" href="#quick-start-2">¶</a>
</h2>"""

h3 = """
<h3 id="create-message-3">
  Create message
  <a class="permalink" href="#create-message-3">¶</a>
</h3>"""

h4 = """
<h4 id="create-message-4">
  Create message
  <a class="permalink" href="#create-message-4">¶</a>
</h4>"""


class NamedEndpointsTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/13. Named Endpoints.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(h2, html)
        self.assertInIgnoreFormatting(h3, html)
        self.assertInIgnoreFormatting(h4, html)
