import unittest
from unittest.mock import Mock, patch

from refract.contrib.apielements import ParseResult
from semantic_version import Version

from apiblueprint_view import _DRAFTER_PATH
from apiblueprint_view.draughtsman import Draughtsman


class DraughtsmanTests(unittest.TestCase):
    def test_parse_valid_blueprint(self):
        dm = Draughtsman(_DRAFTER_PATH)
        parse_result = dm.parse("# My API")

        self.assertIsInstance(parse_result, ParseResult)
        self.assertEqual(parse_result.api.title.defract, "My API")

    def test_parse_valid_blueprint_with_source_maps(self):
        dm = Draughtsman(_DRAFTER_PATH)
        parse_result = dm.parse("# My API", generate_source_map=True)

        self.assertIsInstance(parse_result, ParseResult)
        self.assertEqual(parse_result.api.title.defract, "My API")
        self.assertEqual(
            parse_result.api.title.attributes.get("sourceMap").defract, [[[0, 8]]]
        )

    def test_invalid_drafter_versions(self):
        for version in ["3.2.7", "6.0.0"]:
            mock = Mock(return_value=Version(version))
            with patch(
                "apiblueprint_view.draughtsman.Draughtsman.get_drafter_version", mock,
            ):
                with self.assertRaises(ImportError):
                    Draughtsman(_DRAFTER_PATH)
