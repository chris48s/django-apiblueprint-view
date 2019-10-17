from .base import ApibpTest


retrieve_desc = """
<div class="api-description">
  <p>
    At this point we will utilize our
    <code>Message</code>
    resource model and reference it in
    <code>Response 200</code>.
  </p>
</div>"""

retrieve_json = """{
  "class": [ "message" ],
  "properties": {
    "message": "Hello World!"
  },
  "links": [
    { "rel": "self" , "href": "/message" }
  ]
}""".replace(
    '"', "&quot;"
)

retrieve_resp = (
    """
<div class="api-action-transaction">
  <div class="api-action-request">
    Request
    <span class="api-method api-method-GET">GET</span>
    &#32;
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
       <pre><code>"""
    + retrieve_json
    + """
</code></pre>
    </div>
  </div>
</div>"""
)


class ResourceModelTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/11. Resource Model.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, retrieve_desc, html=True)
        self.assertContains(response, retrieve_resp, html=True)
