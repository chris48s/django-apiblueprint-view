from .base import ApibpTest


example_url = """
<div class="api-action-example">
  Example:
  <a href="/message/1">
    <code>/message/1</code>
  </a>
</div>"""

params_description = """
<div class="api-parameters">
  <h4>Parameters</h4>
  <ul>
    <li>
      <p>
        <strong>id</strong>&#32;
        <code>number</code>
        (
          required
        )
      </p>
      <p>
        An unique identifier of the message.
      </p>
      <p>
        Example: <code>1</code>
      </p>
    </li>
  </ul>
</div>"""


class ParametersTest(ApibpTest):
    def test(self):
        response = self.get_response(
            "apiblueprint_view/tests/fixtures/07. Parameters.md"
        )
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, example_url, html=True)
        self.assertContains(response, params_description, html=True)
