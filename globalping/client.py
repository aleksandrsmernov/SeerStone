import requests
import time


URL = "https://api.globalping.io/v1/measurements"


def create_measurement(target, city, country, measurement_type="ping"):
    payload = {
        "target": target,
        "type": measurement_type,
        "locations": [
            {
                "city": city,
                "country": country
            }
        ]
    }

    if measurement_type == "ping":
        payload["measurementOptions"] = {
            "packets": 5
        }

    response = requests.post(URL, json=payload)

    print("POST status:", response.status_code)

    data = response.json()

    return data["id"]


def wait_for_result(measurement_id):
    result_url = f"{URL}/{measurement_id}"

    while True:
        response = requests.get(result_url)
        data = response.json()

        print("Status:", data["status"])

        if data["status"] == "finished":
            return data

        time.sleep(1)