from .base import ApibpTest


h2 = """
<h2 id="quick-start-2">
  Quick start&nbsp;
  <a class="permalink" href="#quick-start-2">&para;</a>
</h2>"""

h3 = """
<h3 id="create-message-3">
  Create message&nbsp;
  <a class="permalink" href="#create-message-3">&para;</a>
</h3>"""

h4 = """
<h4 id="create-message-4">
  Create message&nbsp;
  <a class="permalink" href="#create-message-4">&para;</a>
</h4>"""


class NamedEndpointsTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/13. Named Endpoints.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, h2, html=True)
        self.assertContains(response, h3, html=True)
        self.assertContains(response, h4, html=True)
