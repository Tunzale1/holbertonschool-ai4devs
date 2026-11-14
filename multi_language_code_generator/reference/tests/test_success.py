
import unittest
from reference.log_analyzer import LogAnalyzer

class TestSuccess(unittest.TestCase):
    def test_successful_request(self):
        entry = {
            "timestamp": "2026-11-15T10:00:00Z",
            "ip": "192.168.1.10",
            "method": "GET",
            "path": "/home",
            "status": 200
        }
        result = LogAnalyzer().analyze([entry])
        self.assertEqual(result["successful_requests"], 1)

if __name__ == "__main__":
    unittest.main()
