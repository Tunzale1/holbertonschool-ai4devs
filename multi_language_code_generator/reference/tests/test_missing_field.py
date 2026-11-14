
import unittest
from reference.log_analyzer import LogAnalyzer

class TestMissingField(unittest.TestCase):
    def test_missing_ip(self):
        entry = {
            "timestamp": "2026-11-15T10:00:00Z",
            "method": "GET",
            "path": "/home",
            "status": 200
        }
        result = LogAnalyzer().analyze([entry])
        self.assertEqual(result["malformed_entries"], 1)

if __name__ == "__main__":
    unittest.main()
