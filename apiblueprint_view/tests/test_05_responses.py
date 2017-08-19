from .base import ApibpTest


text_response = """
<div class="api-action-response">
  Response
  <code class="api-http-code">200</code>
  <div class="api-action-headers">
    Headers:
    <pre><code>Content-Type: text/plain
X-My-Message-Header: 42
</code></pre>
  </div>
  <div class="api-action-body">
    Body:
    <pre><code>Hello World!
</code></pre>
  </div>
</div>"""

json_response = """
<div class="api-action-response">
  Response
  <code class="api-http-code">200</code>
  <div class="api-action-headers">
    Headers:
    <pre><code>Content-Type: application/json
X-My-Message-Header: 42
</code></pre>
  </div>
  <div class="api-action-body">
    Body:
    <pre><code>{ "message": "Hello World!" }
</code></pre>
  </div>
</div>"""


class ResponsesTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/05. Responses.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(text_response, html)
        self.assertInIgnoreFormatting(json_response, html)
