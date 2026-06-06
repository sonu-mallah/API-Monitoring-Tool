import requests
import time
import json
from datetime import datetime

url = input("Enter API URL: ")

try:
    start_time = time.time()

    response = requests.get(url, timeout=5)

    end_time = time.time()

    response_time = round((end_time - start_time) * 1000, 2)

    # Response Category
    if 200 <= response.status_code < 300:
        category = "Success"
    elif 300 <= response.status_code < 400:
        category = "Redirection"
    elif 400 <= response.status_code < 500:
        category = "Client Error"
    else:
        category = "Server Error"

    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "url": url,
        "status_code": response.status_code,
        "response_category": category,
        "response_time_ms": response_time,
        "response_size_bytes": len(response.content),
        "api_status": "UP" if response.status_code == 200 else "DOWN"
    }

    try:
        response.json()
        report["json_valid"] = True
    except:
        report["json_valid"] = False

    print("\n===== API HEALTH REPORT =====")
    print(f"Timestamp: {report['timestamp']}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Category: {category}")
    print(f"Response Time: {response_time} ms")
    print(f"Response Size: {len(response.content)} bytes")
    print(f"API Status: {report['api_status']}")
    print(f"JSON Valid: {report['json_valid']}")

    # Save latest report
    with open("report.json", "w") as file:
        json.dump(report, file, indent=4)

    # Load existing history
    try:
        with open("history.json", "r") as file:
            history = json.load(file)
    except:
        history = []

    # Add current report
    history.append(report)

    # Save updated history
    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)

    print("\nReport saved to report.json")
    print("History updated in history.json")

except requests.exceptions.Timeout:
    print("API Status: DOWN (Timeout)")

except requests.exceptions.ConnectionError:
    print("API Status: DOWN (Connection Error)")

except Exception as e:
    print("Error:", e)