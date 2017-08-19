from .base import ApibpTest


get_schema = """
<div class="api-action-schema">
  Schema:
  <pre><code>{
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "title": {
            "type": "string"
        },
        "content": {
            "type": "string"
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    }
}
</code></pre>
</div>"""

patch_schema = """
<div class="api-action-schema">
  Schema:
  <pre><code>{
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "content": {
            "type": "string"
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "additionalProperties": false
}
</code></pre>
</div>"""


class JsonSchemaTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/14. JSON Schema.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(get_schema, html)
        self.assertInIgnoreFormatting(patch_schema, html)
