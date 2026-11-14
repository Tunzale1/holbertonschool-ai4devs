
import unittest
from reference.log_analyzer import LogAnalyzer

class TestServerError(unittest.TestCase):
    def test_500_error(self):
        entry = {
            "timestamp": "2026-11-15T10:00:00Z",
            "ip": "192.168.1.10",
            "method": "GET",
            "path": "/server",
            "status": 500
        }
        result = LogAnalyzer().analyze([entry])
        self.assertEqual(result["server_errors"], 1)

if __name__ == "__main__":
    unittest.main()
