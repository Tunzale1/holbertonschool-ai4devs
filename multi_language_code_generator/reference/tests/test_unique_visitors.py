
import unittest
from reference.log_analyzer import LogAnalyzer

class TestUniqueVisitors(unittest.TestCase):
    def test_duplicate_ips(self):
        base = {
            "timestamp": "2026-11-15T10:00:00Z",
            "method": "GET",
            "path": "/home",
            "status": 200
        }
        entries = [
            {**base, "ip": "192.168.1.10"},
            {**base, "ip": "192.168.1.10"},
            {**base, "ip": "192.168.1.11"}
        ]
        result = LogAnalyzer().analyze(entries)
        self.assertEqual(result["unique_visitors"], 2)

if __name__ == "__main__":
    unittest.main()
