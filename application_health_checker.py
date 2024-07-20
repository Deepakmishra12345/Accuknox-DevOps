import requests
import time

# URL of the application to check
URL = "https://www.youtube.com/"

def check_application_status():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Error: {e}")

def monitor_application():
    while True:
        print("Checking application status...")
        check_application_status()
        time.sleep(60)

if __name__ == "__main__":
    monitor_application()
