from .base import ApibpTest


example = """
  <code>/message</code>
  <div class="api-action-example">
    Example:
    <a href="https://foo.bar/baz/message">
      <code>https://foo.bar/baz/message</code>
    </a>
  </div>
"""


class HostnameTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/host.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(example, html)
