
import unittest
from reference.log_analyzer import LogAnalyzer

class TestClientError(unittest.TestCase):
    def test_404_error(self):
        entry = {
            "timestamp": "2026-11-15T10:00:00Z",
            "ip": "192.168.1.10",
            "method": "GET",
            "path": "/missing",
            "status": 404
        }
        result = LogAnalyzer().analyze([entry])
        self.assertEqual(result["client_errors"], 1)

if __name__ == "__main__":
    unittest.main()
