from apiblueprint_view import _DRAFTER_PATH
from apiblueprint_view.draughtsman import Draughtsman

from .base import ApibpTest

body_json = """{
  "percent_off": 25,
  "redeem_by": 0,
  "id": "250FF",
  "created": 1415203908
}""".replace(
    '"', "&quot;"
)

coupon_body = (
    """
<div class="api-action-body">
  Body:
  <pre><code>"""
    + body_json
    + """</code></pre>
</div>
"""
)


schema_json = """{
  "$schema": "http://json-schema.org/draft-%s/schema#",
  "type": "object",
  "properties": {
    "percent_off": {
      "type": "number"
    },
    "redeem_by": {
      "type": "number"
    },
    "id": {
      "type": "string"
    },
    "created": {
      "type": "number"
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


class DataStructuresTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/10. Data Structures.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, coupon_body, html=True)
        self.assertContains(response, get_coupon_schema(), html=True)
