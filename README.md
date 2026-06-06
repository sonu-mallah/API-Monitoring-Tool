API Monitoring Tool

Overview

API Monitoring Tool is a Python-based utility that monitors REST API endpoints and generates health reports. The application measures response time, validates JSON responses, categorizes HTTP status codes, and maintains monitoring history for troubleshooting and analysis.

Features

- Monitor REST API availability
- Measure API response time
- Validate JSON responses
- Detect API health status (UP/DOWN)
- Categorize HTTP responses
- Track response size
- Generate structured JSON reports
- Maintain historical monitoring logs
- Handle timeout and connection errors

Technologies Used

- Python 3
- Requests Library
- JSON
- Git & GitHub

Project Structure

API-Monitoring-Tool/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

Generated during execution:

report.json
history.json

How It Works

1. User enters an API URL.
2. The application sends an HTTP GET request.
3. Response time is measured.
4. HTTP status code is analyzed.
5. Response category is determined.
6. JSON response validation is performed.
7. API health report is generated.
8. Monitoring history is stored locally.

Example Metrics

- Timestamp
- Status Code
- Response Category
- Response Time
- Response Size
- API Status
- JSON Validation Status

Skills Demonstrated

- Python Programming
- REST API Integration
- JSON Processing
- File Handling
- Exception Handling
- Debugging
- Monitoring & Logging
- Git Version Control

Future Improvements

- Multi-API Monitoring
- Dashboard Visualization
- Email Alerts
- Database Storage
- Scheduled Monitoring

Author

Sonu Mallah