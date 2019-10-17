from .base import ApibpTest


body_json = """[
  {
    "id": "250FF",
    "created": 1415203908,
    "percent_off": 25,
    "redeem_by": 0
  }
]""".replace(
    '"', "&quot;"
)

coupons_body = (
    """
<div class="api-action-body">
  Body:
  <pre><code>"""
    + body_json
    + """</code></pre>
</div>"""
)


schema_json = """{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array"
}""".replace(
    '"', "&quot;"
)

coupons_schema = (
    """
<div class="api-action-schema">
  Schema:
  <pre><code>"""
    + schema_json
    + """</code></pre>
</div>"""
)


class AdvancedAttributesTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/09. Advanced Attributes.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, coupons_body, html=True)
        self.assertContains(response, coupons_schema, html=True)
