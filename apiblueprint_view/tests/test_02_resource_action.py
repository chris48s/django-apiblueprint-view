from .base import ApibpTest


put_response = """
<div class="api-action-transaction">
  <div class="api-action-request">
    Request
    <span class="api-method api-method-PUT">PUT</span>
    &#32;
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
  </div>
  <div class="api-action-response">
    Response
    <code class="api-http-code">204</code>
  </div>
</div>"""


class ResourceActionTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/02. Resource and Actions.md"
        )
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        # html should contain 4 description blocks:
        # the group, the resource and 2 actions
        self.assertEqual(4, html.count('<div class="api-description">'))

        self.assertContains(response, put_response, html=True)
