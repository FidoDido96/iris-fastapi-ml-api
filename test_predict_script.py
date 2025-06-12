import requests
import json

url = "http://127.0.0.1:5000/v1/iris/predict"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data = {
    "data": [
        [float(4.8), float(3.1), float(4.0), float(0.3)],
        [float(2.1), float(3.2), float(1.1), float(1.5)]
    ]
}

print("Data being sent:", json.dumps(data))

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print("Response Body:", e.response.json())
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")