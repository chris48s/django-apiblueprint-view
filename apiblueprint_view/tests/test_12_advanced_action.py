"""
TODO: pending solution to issue #7


from .base import ApibpTest


class AdvancedActionTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/12. Advanced Action.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        print(html)
"""
