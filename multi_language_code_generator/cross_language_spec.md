
# Cross-Language Specification - Log Analyzer

## 1. Algorithm Description

Develop a Log Analyzer that processes server log entries and calculates important traffic statistics.

The algorithm must:
- Count the total number of valid requests.
- Count successful requests (HTTP 2xx).
- Count redirect requests (HTTP 3xx).
- Count client errors (HTTP 4xx).
- Count server errors (HTTP 5xx).
- Identify the number of unique visitors based on IP addresses.
- Calculate the error rate as a percentage.
- Count and report malformed log entries.

The algorithm must produce consistent results regardless of the programming language used.

## 2. Input Format

The input is a JSON array containing server log entries.

Each entry must contain:
- `timestamp`: Date and time of the request.
- `ip`: Visitor's IP address.
- `method`: HTTP request method (GET, POST, PUT, DELETE, etc.).
- `path`: Requested resource.
- `status`: HTTP response status code (integer between 100 and 599).

Example:

[
  {
    "timestamp": "2026-11-15T10:00:00Z",
    "ip": "192.168.1.10",
    "method": "GET",
    "path": "/home",
    "status": 200
  },
  {
    "timestamp": "2026-11-15T10:05:00Z",
    "ip": "192.168.1.11",
    "method": "POST",
    "path": "/login",
    "status": 401
  },
  {
    "timestamp": "2026-11-15T10:10:00Z",
    "ip": "192.168.1.10",
    "method": "GET",
    "path": "/dashboard",
    "status": 500
  }
]

## 3. Output Format

The algorithm must return a JSON object containing the calculated statistics.

Example:

{
  "total_requests": 3,
  "successful_requests": 1,
  "redirect_requests": 0,
  "client_errors": 1,
  "server_errors": 1,
  "unique_visitors": 2,
  "error_rate": 66.67,
  "malformed_entries": 0
}

Error rate formula:

error_rate = ((client_errors + server_errors) / total_requests) * 100

If there are no valid requests, the error rate must be 0.

## 4. Edge Cases

The implementation must handle the following situations:

- Empty input: Return zero for all statistics.
- Malformed JSON: Return a clear input error.
- Missing fields: Treat the affected entry as malformed.
- Invalid IP address: Treat the affected entry as malformed.
- Invalid HTTP status code: Treat the affected entry as malformed.
- Duplicate visitors: Count the same IP address only once.
- Mixed HTTP status codes: Correctly classify 2xx, 3xx, 4xx, and 5xx responses.
- All requests invalid: Return zero valid requests and report malformed entries.

Malformed entries must not contribute to request statistics.

## 5. Test Cases

### Test Case 1 - Normal Log Entries

Input:
- 3 valid requests.
- Status codes: 200, 401, 500.
- 2 unique IP addresses.

Expected Output:
- total_requests: 3
- successful_requests: 1
- redirect_requests: 0
- client_errors: 1
- server_errors: 1
- unique_visitors: 2
- error_rate: 66.67
- malformed_entries: 0

### Test Case 2 - Empty Input

Input:
- Empty JSON array: []

Expected Output:
- total_requests: 0
- successful_requests: 0
- redirect_requests: 0
- client_errors: 0
- server_errors: 0
- unique_visitors: 0
- error_rate: 0
- malformed_entries: 0

### Test Case 3 - Duplicate Visitors

Input:
- 4 valid requests.
- IP addresses: 192.168.1.10, 192.168.1.10, 192.168.1.11, 192.168.1.10.
- Status codes: 200, 200, 200, 404.

Expected Output:
- total_requests: 4
- successful_requests: 3
- redirect_requests: 0
- client_errors: 1
- server_errors: 0
- unique_visitors: 2
- error_rate: 25.00
- malformed_entries: 0

### Test Case 4 - Mixed Status Codes

Input:
- 5 valid requests.
- Status codes: 200, 301, 404, 500, 201.

Expected Output:
- total_requests: 5
- successful_requests: 2
- redirect_requests: 1
- client_errors: 1
- server_errors: 1
- unique_visitors: 5
- error_rate: 40.00
- malformed_entries: 0

### Test Case 5 - Malformed Entries

Input:
- 3 entries.
- 2 valid entries with status codes 200 and 404.
- 1 entry missing the IP address.

Expected Output:
- total_requests: 2
- successful_requests: 1
- redirect_requests: 0
- client_errors: 1
- server_errors: 0
- unique_visitors: 2
- error_rate: 50.00
- malformed_entries: 1

### Test Case 6 - All Requests Invalid

Input:
- 2 entries.
- Both entries have invalid HTTP status codes.

Expected Output:
- total_requests: 0
- successful_requests: 0
- redirect_requests: 0
- client_errors: 0
- server_errors: 0
- unique_visitors: 0
- error_rate: 0
- malformed_entries: 2

## 6. Cross-Language Compatibility Requirements

The algorithm must produce identical results when implemented in different programming languages.

Supported implementation languages:
- Python
- JavaScript
- Java
- C++

All implementations must:
- Follow the same input and output formats.
- Apply identical validation rules.
- Use the same error-rate calculation.
- Pass all six test cases.
- Handle edge cases consistently.

## 7. Success Criteria

The specification is considered successfully implemented when:
- All valid log entries are processed correctly.
- Invalid entries are identified and excluded.
- All statistics match the expected outputs.
- All six test cases pass.
- Different language implementations produce equivalent results.
