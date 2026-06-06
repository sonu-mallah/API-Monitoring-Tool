# API Monitoring Tool

## Overview

A Python-based monitoring utility that checks REST API availability, measures response time, validates JSON responses, and generates structured health reports.

## Features

- Monitor REST API availability
- Measure API response time
- Validate JSON responses
- Detect API health status (UP/DOWN)
- Categorize HTTP responses
- Track response size
- Generate structured JSON reports
- Maintain historical monitoring logs
- Handle timeout and connection errors

## Technologies Used

- Python 3
- Requests
- JSON
- Git & GitHub

## Project Structure

```text
API-Monitoring-Tool/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

Generated during execution:

```text
report.json
history.json
```

## How It Works

1. User enters an API URL
2. Application sends an HTTP GET request
3. Response time is measured
4. HTTP status code is analyzed
5. JSON validation is performed
6. Health report is generated
7. Monitoring history is stored locally

## Skills Demonstrated

- Python Programming
- REST APIs
- JSON Processing
- Exception Handling
- File Handling
- Debugging
- Monitoring & Logging
- Git Version Control

## Future Improvements

- Multi-API Monitoring
- Email Alerts
- Dashboard Visualization
- Database Storage

## Author

Sonu Mallah