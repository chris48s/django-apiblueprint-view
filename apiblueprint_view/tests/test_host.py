from .base import ApibpTest


url = "<code>/message</code>"

example = """
  <div class="api-action-example">
    Example:
    <a href="https://foo.bar/baz/message">
      <code>https://foo.bar/baz/message</code>
    </a>
  </div>
"""


class HostnameTest(ApibpTest):
    def test(self):
        response = self.get_response("apiblueprint_view/tests/fixtures/host.md")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, url, html=True)
        self.assertContains(response, example, html=True)
