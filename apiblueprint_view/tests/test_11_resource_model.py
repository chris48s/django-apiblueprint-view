from .base import ApibpTest


retrieve_resp = """
<div class="api-description">
  <p>
    At this point we will utilize our
    <code>Message</code>
    resource model and reference it in
    <code>Response 200</code>.
  </p>
</div>
<div class="api-action-transaction">
  <div class="api-action-request">
    Request
    <span class="api-method api-method-GET">GET</span>
    <code>/message</code>
  </div>
  <div class="api-action-response">
    Response
    <code class="api-http-code">200</code>
    <div class="api-action-headers">
      Headers:
      <pre><code>Content-Type: application/vnd.siren+json
Location: http://api.acme.com/message
</code></pre>
    </div>
    <div class="api-description">
      <p>
        This is the
        <code>application/vnd.siren+json</code>
        message resource representation.
      </p>
    </div>
    <div class="api-action-body">
       Body:
       <pre><code>{
  "class": [ "message" ],
  "properties": {
    "message": "Hello World!"
  },
  "links": [
    { "rel": "self" , "href": "/message" }
  ]
}
</code></pre>
    </div>
  </div>
</div>"""


class ResourceModelTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/11. Resource Model.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(retrieve_resp, html)
