from .base import ApibpTest


custom_schema_attribute = '"description": "This is a custom schema!",'


class AdvancedSchemaTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/15. Advanced JSON Schema.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(custom_schema_attribute, html)
