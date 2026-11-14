
import unittest
from reference.log_analyzer import LogAnalyzer

class TestRedirect(unittest.TestCase):
    def test_redirect_status(self):
        entry = {
            "timestamp": "2026-11-15T10:00:00Z",
            "ip": "192.168.1.10",
            "method": "GET",
            "path": "/redirect",
            "status": 301
        }
        result = LogAnalyzer().analyze([entry])
        self.assertEqual(result["redirect_requests"], 1)

if __name__ == "__main__":
    unittest.main()
