import unittest
from apiblueprint_view import dm
from refract.contrib.apielements import ParseResult


class DraughtsmanTests(unittest.TestCase):
    def test_parse_valid_blueprint(self):
        parse_result = dm.parse("# My API")

        self.assertIsInstance(parse_result, ParseResult)
        self.assertEqual(parse_result.api.title.defract, "My API")
