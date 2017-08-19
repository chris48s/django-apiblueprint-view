from .base import ApibpTest


text_header = """
<div class="api-action-headers">
  Headers:
  <pre><code>Accept: text/plain
</code></pre>
</div>"""

json_header = """
<div class="api-action-headers">
  Headers:
  <pre><code>Accept: application/json
</code></pre>
</div>"""

update_request = """
<div class="api-action-request">
  <h5 id="update-plain-text-message-5">
    Update Plain Text Message
    <a class="permalink" href="#update-plain-text-message-5">¶</a>
  </h5>
  Request
  <span class="api-method api-method-PUT">PUT</span>
  <code>/message</code>
  <div class="api-action-headers">
    Headers:
    <pre><code>Content-Type: text/plain
</code></pre>
  </div>
  <div class="api-action-body">
    Body:
    <pre><code>All your base are belong to us.
</code></pre>
  </div>
</div>"""


class RequestsTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/06. Requests.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(text_header, html)
        self.assertInIgnoreFormatting(json_header, html)
        self.assertInIgnoreFormatting(update_request, html)
