from .base import ApibpTest


group_name = """
<h3 id="my-message-3">
  My Message&nbsp;
  <a class="permalink" href="#my-message-3">&para;</a>
</h3>"""

get_action = """
<h4 id="retrieve-a-message-4">
  Retrieve a Message&nbsp;
  <a class="permalink" href="#retrieve-a-message-4">&para;</a>
</h4>"""

put_action = """
<h4 id="update-a-message-4">
  Update a Message&nbsp;
  <a class="permalink" href="#update-a-message-4">&para;</a>
</h4>"""


class NamedResourceTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/03. Named Resource and Actions.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, group_name, html=True)
        self.assertContains(response, get_action, html=True)
        self.assertContains(response, put_action, html=True)
