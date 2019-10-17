from .base import ApibpTest


get_schema_json = """{
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
}""".replace(
    '"', "&quot;"
)

get_schema = (
    """
<div class="api-action-schema">
  Schema:
  <pre><code>"""
    + get_schema_json
    + """
</code></pre>
</div>"""
)


patch_schema_json = """{
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
}""".replace(
    '"', "&quot;"
)

patch_schema = (
    """
<div class="api-action-schema">
  Schema:
  <pre><code>"""
    + patch_schema_json
    + """
</code></pre>
</div>"""
)


class JsonSchemaTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/14. JSON Schema.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, get_schema, html=True)
        self.assertContains(response, patch_schema, html=True)
