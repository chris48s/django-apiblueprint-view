from .base import ApibpTest
from apiblueprint_view import _DRAFTER_PATH
from apiblueprint_view.draughtsman import Draughtsman



body_json = """{
    "id": "250FF",
    "created": 1415203908,
    "percent_off": 25,
    "redeem_by": null
}""".replace(
    '"', "&quot;"
)

coupon_body = (
    """
<div class="api-action-body">
  Body:
  <pre><code>"""
    + body_json
    + """
</code></pre>
</div>"""
)


schema_json = """{
  "$schema": "http://json-schema.org/draft-%s/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "created": {
      "type": "number",
      "description": "Time stamp"
    },
    "percent_off": {
      "type": "number",
      "description": "A positive integer between 1 and 100 that represents the discount\\nthe coupon will apply."
    },
    "redeem_by": {
      "type": "number",
      "description": "Date after which the coupon can no longer be redeemed"
    }
  },
  "required": [
    "id"
  ]
}""".replace(
    '"', "&quot;"
)

coupon_schema = (
    """
<div class="api-action-schema">
  Schema:
  <pre><code>"""
    + schema_json
    + """</code></pre>
</div>"""
)


def get_coupon_schema():
    dm = Draughtsman(_DRAFTER_PATH)
    drafter_version = dm.get_drafter_version()
    if drafter_version.major == 5:
        return coupon_schema % "07"
    else:
        return coupon_schema % "04"


class AttributesTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/08. Attributes.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, coupon_body, html=True)
        self.assertContains(response, get_coupon_schema(), html=True)
