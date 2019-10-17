from django.core.exceptions import SuspiciousFileOperation
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
        response = self.get_response("apiblueprint_view/tests/fixtures/parent.md")
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertContains(response, response_body, html=True)
        self.assertNotIn(comment, html)

    def test_include_setting_on(self):
        with self.settings(APIBP_PROCESS_INCLUDES=True):
            response = self.get_response("apiblueprint_view/tests/fixtures/parent.md")
            self.assertEqual(response.status_code, 200)
            html = self.get_html(response)

            self.assertContains(response, response_body, html=True)
            self.assertNotIn(comment, html)

    def test_include_setting_off(self):
        with self.settings(APIBP_PROCESS_INCLUDES=False):
            response = self.get_response("apiblueprint_view/tests/fixtures/parent.md")
            self.assertEqual(response.status_code, 200)
            html = self.get_html(response)

            self.assertNotContains(response, response_body, html=True)
            self.assertIn(comment, html)

    def test_include_suspicious_outside_project_dir(self):
        with self.assertRaises(SuspiciousFileOperation):
            self.get_response("apiblueprint_view/tests/fixtures/suspicious.md")

    def test_include_suspicious_not_in_whitelist(self):
        with self.settings(APIBP_INCLUDE_WHITELIST=[".apibp", ".json"]):
            with self.assertRaises(SuspiciousFileOperation):
                self.get_response("apiblueprint_view/tests/fixtures/parent.md")
