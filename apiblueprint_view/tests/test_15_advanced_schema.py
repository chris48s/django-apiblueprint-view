from .base import ApibpTest


custom_schema_attribute = (
    "&quot;description&quot;: &quot;This is a custom schema!&quot;,"
)


class AdvancedSchemaTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/15. Advanced JSON Schema.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, custom_schema_attribute)
