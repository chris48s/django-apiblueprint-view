from .base import ApibpTest


coupons_body = """
<div class="api-action-body">
  Body:
  <pre><code>[
  {
    "id": "250FF",
    "created": 1415203908,
    "percent_off": 25,
    "redeem_by": 0
  }
]</code></pre>
</div>"""

coupons_schema = """
<div class="api-action-schema">
  Schema:
  <pre><code>{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array"
}</code></pre>
</div>"""


class AdvancedAttributesTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/09. Advanced Attributes.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(coupons_body, html)
        self.assertInIgnoreFormatting(coupons_schema, html)
