
import json
import ipaddress
from datetime import datetime


class LogAnalyzer:

    def validate_entry(self, entry):
        """Check whether a log entry contains valid information."""

        if not isinstance(entry, dict):
            return False

        required_fields = ["timestamp", "ip", "method", "path", "status"]

        if any(field not in entry for field in required_fields):
            return False

        if not all(
            isinstance(entry[field], str) and entry[field].strip()
            for field in ["timestamp", "ip", "method", "path"]
        ):
            return False

        try:
            ipaddress.ip_address(entry["ip"])
        except ValueError:
            return False

        try:
            timestamp = entry["timestamp"].replace("Z", "+00:00")
            datetime.fromisoformat(timestamp)
        except ValueError:
            return False

        status = entry["status"]

        if isinstance(status, bool) or not isinstance(status, int):
            return False

        if not 100 <= status <= 599:
            return False

        return True

    def analyze(self, entries):
        """Analyze server logs and calculate statistics."""

        if not isinstance(entries, list):
            raise ValueError("Input must be a JSON array.")

        total = 0
        successful = 0
        redirects = 0
        client_errors = 0
        server_errors = 0
        malformed = 0
        visitors = set()

        for entry in entries:

            if not self.validate_entry(entry):
                malformed += 1
                continue

            total += 1
            visitors.add(entry["ip"])

            status = entry["status"]

            if 200 <= status <= 299:
                successful += 1
            elif 300 <= status <= 399:
                redirects += 1
            elif 400 <= status <= 499:
                client_errors += 1
            elif 500 <= status <= 599:
                server_errors += 1

        errors = client_errors + server_errors

        error_rate = round((errors / total) * 100, 2) if total else 0

        return {
            "total_requests": total,
            "successful_requests": successful,
            "redirect_requests": redirects,
            "client_errors": client_errors,
            "server_errors": server_errors,
            "unique_visitors": len(visitors),
            "error_rate": error_rate,
            "malformed_entries": malformed
        }

    def analyze_json(self, json_data):
        """Parse JSON input and analyze its log entries."""

        try:
            entries = json.loads(json_data)
        except (json.JSONDecodeError, TypeError):
            raise ValueError("Invalid JSON input.")

        return self.analyze(entries)
