
import unittest
from reference.log_analyzer import LogAnalyzer

class TestInvalidIP(unittest.TestCase):
    def test_invalid_ip_address(self):
        entry = {
            "timestamp": "2026-11-15T10:00:00Z",
            "ip": "invalid-ip",
            "method": "GET",
            "path": "/home",
            "status": 200
        }
        result = LogAnalyzer().analyze([entry])
        self.assertEqual(result["malformed_entries"], 1)
        self.assertEqual(result["total_requests"], 0)

if __name__ == "__main__":
    unittest.main()
