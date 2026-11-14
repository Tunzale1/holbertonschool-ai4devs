
import unittest
from reference.log_analyzer import LogAnalyzer

class TestInvalidTimestamp(unittest.TestCase):
    def test_invalid_timestamp(self):
        entry = {
            "timestamp": "not-a-date",
            "ip": "192.168.1.10",
            "method": "GET",
            "path": "/home",
            "status": 200
        }
        result = LogAnalyzer().analyze([entry])
        self.assertEqual(result["malformed_entries"], 1)

if __name__ == "__main__":
    unittest.main()
