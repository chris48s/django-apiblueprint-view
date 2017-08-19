from .base import ApibpTest


messages_group_title = """
<h2 id="messages-2">
  Messages
  <a class="permalink" href="#messages-2">¶</a>
</h2>"""

users_group_title = """
<h2 id="users-2">
  Users
  <a class="permalink" href="#users-2">¶</a>
</h2>"""

users_group_description = """
<div class="api-description">
  <p>
    Group of all user-related resources.
  </p>
  <p>
    This is the second group in this blueprint. For now, no resources were defined
here and as such we will omit it from the next installment of this course.
  </p>
</div>"""


class GroupingResourcesTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/04. Grouping Resources.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(messages_group_title, html)
        self.assertInIgnoreFormatting(users_group_title, html)
        self.assertInIgnoreFormatting(users_group_description, html)
