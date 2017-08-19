from .base import ApibpTest


action_request = """
<div class="api-action-request">
  Request
  <span class="api-method api-method-GET">GET</span>
  <code>/message</code>
</div>"""

action_response = """
<div class="api-action-response">
  Response
  <code class="api-http-code">200</code>
  <div class="api-action-headers">
    Headers:
    <pre><code>Content-Type: text/plain
</code></pre>
  </div>
  <div class="api-action-body">
    Body:
    <pre><code>Hello World!
</code></pre>
  </div>
</div>"""


class SimplestTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/01. Simplest API.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(action_request, html)
        self.assertInIgnoreFormatting(action_response, html)
