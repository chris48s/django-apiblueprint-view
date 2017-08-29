from .base import ApibpTest


response_body = """
<div class="api-action-body">
  Body:
  <pre><code>Hello World!
</code></pre>
</div>"""

comment = "<!-- include(child.md) -->"


class IncludesTest(ApibpTest):

    def test_include_no_setting(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/parent.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(response_body, html)
        self.assertNotInIgnoreFormatting(comment, html)

    def test_include_setting_on(self):
        with self.settings(APIBP_PROCESS_INCLUDES=True):
            response = self.get_response(
                'apiblueprint_view/tests/fixtures/parent.md')
            self.assertEqual(response.status_code, 200)
            html = self.get_html(response)

            self.assertInIgnoreFormatting(response_body, html)
            self.assertNotInIgnoreFormatting(comment, html)

    def test_include_setting_off(self):
        with self.settings(APIBP_PROCESS_INCLUDES=False):
            response = self.get_response(
                'apiblueprint_view/tests/fixtures/parent.md')
            self.assertEqual(response.status_code, 200)
            html = self.get_html(response)

            self.assertNotInIgnoreFormatting(response_body, html)
            self.assertInIgnoreFormatting(comment, html)