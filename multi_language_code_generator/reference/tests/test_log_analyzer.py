
import unittest
from reference.log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()

    def make_entry(self, ip="192.168.1.10", status=200):
        return {
            "timestamp": "2026-11-15T10:00:00Z",
            "ip": ip,
            "method": "GET",
            "path": "/home",
            "status": status
        }

    # Test 1: Empty input
    def test_empty_input(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["error_rate"], 0)

    # Test 2: One successful request
    def test_successful_request(self):
        result = self.analyzer.analyze([self.make_entry()])
        self.assertEqual(result["successful_requests"], 1)

    # Test 3: Client error
    def test_client_error(self):
        result = self.analyzer.analyze(
            [self.make_entry(status=404)]
        )
        self.assertEqual(result["client_errors"], 1)

    # Test 4: Server error
    def test_server_error(self):
        result = self.analyzer.analyze(
            [self.make_entry(status=500)]
        )
        self.assertEqual(result["server_errors"], 1)

    # Test 5: Redirect request
    def test_redirect_request(self):
        result = self.analyzer.analyze(
            [self.make_entry(status=301)]
        )
        self.assertEqual(result["redirect_requests"], 1)

    # Test 6: Duplicate visitors
    def test_duplicate_visitors(self):
        entries = [
            self.make_entry("192.168.1.10"),
            self.make_entry("192.168.1.10"),
            self.make_entry("192.168.1.11")
        ]
        result = self.analyzer.analyze(entries)
        self.assertEqual(result["unique_visitors"], 2)

    # Test 7: Invalid IP address
    def test_invalid_ip(self):
        result = self.analyzer.analyze(
            [self.make_entry(ip="invalid-ip")]
        )
        self.assertEqual(result["malformed_entries"], 1)
        self.assertEqual(result["total_requests"], 0)

    # Test 8: Missing required field
    def test_missing_field(self):
        entry = self.make_entry()
        del entry["ip"]

        result = self.analyzer.analyze([entry])
        self.assertEqual(result["malformed_entries"], 1)

    # Test 9: Invalid HTTP status
    def test_invalid_status(self):
        result = self.analyzer.analyze(
            [self.make_entry(status=700)]
        )
        self.assertEqual(result["malformed_entries"], 1)

    # Test 10: Error rate calculation
    def test_error_rate(self):
        entries = [
            self.make_entry(status=200),
            self.make_entry(status=404),
            self.make_entry(status=500),
            self.make_entry(status=201)
        ]

        result = self.analyzer.analyze(entries)
        self.assertEqual(result["error_rate"], 50.0)

    # Test 11: Malformed timestamp
    def test_invalid_timestamp(self):
        entry = self.make_entry()
        entry["timestamp"] = "not-a-date"

        result = self.analyzer.analyze([entry])
        self.assertEqual(result["malformed_entries"], 1)

    # Test 12: Invalid JSON
    def test_invalid_json(self):
        with self.assertRaises(ValueError):
            self.analyzer.analyze_json("{invalid json}")

    # Test 13: JSON input is not an array
    def test_json_object_instead_of_array(self):
        with self.assertRaises(ValueError):
            self.analyzer.analyze_json('{"status": 200}')


if __name__ == "__main__":
    unittest.main()
