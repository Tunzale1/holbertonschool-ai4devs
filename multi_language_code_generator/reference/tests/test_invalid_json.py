
import unittest
from reference.log_analyzer import LogAnalyzer

class TestInvalidJSON(unittest.TestCase):
    def test_invalid_json_input(self):
        with self.assertRaises(ValueError):
            LogAnalyzer().analyze_json("{invalid json}")

if __name__ == "__main__":
    unittest.main()
