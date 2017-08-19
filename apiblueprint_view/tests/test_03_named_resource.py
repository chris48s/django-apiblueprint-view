from .base import ApibpTest


group_name = """
<h3 id="my-message-3">
  My Message
  <a class="permalink" href="#my-message-3">¶</a>
</h3>"""

get_action = """
<h4 id="retrieve-a-message-4">
  Retrieve a Message
  <a class="permalink" href="#retrieve-a-message-4">¶</a>
</h4>"""

put_action = """
<h4 id="update-a-message-4">
  Update a Message
  <a class="permalink" href="#update-a-message-4">¶</a>
</h4>"""


class NamedResourceTest(ApibpTest):

    def test(self):
        response = self.get_response(
            'apiblueprint_view/tests/fixtures/03. Named Resource and Actions.md')
        self.assertEqual(response.status_code, 200)
        html = self.get_html(response)

        self.assertInIgnoreFormatting(group_name, html)
        self.assertInIgnoreFormatting(get_action, html)
        self.assertInIgnoreFormatting(put_action, html)
