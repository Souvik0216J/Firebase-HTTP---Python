import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

KEY = os.getenv("API_URL")

# Firebase Realtime Database URL (Everytime it's end with .json for REST API)
firebase_url = f"{KEY}/sensor_readings.json"

def sendData():
    temp = input("\nEnter temperature: ")
    humi = input("\nEnter humidity: ")
    
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    
    data = {
        "temperature": temp,
        "humidity": humi,
    }

    # Send data (POST for add a new record and PUT for replaces data)
    response = requests.post(firebase_url, json=data)

    if response.status_code == 200:
        print("Data sent successfully!")
        print("Response:", response.json())
    else:
        print("Failed to send data. Status code:", response.status_code)
        print("Response text:", response.text)


def readData():
    response = requests.get(firebase_url)
    if response.status_code == 200:
        data = response.json()
        print("Data from Firebase:", data)
    else:
        print("Failed to fetch data")


if __name__ == "__main__":
    while(True):
        print("\n1..Send data\n2..Read Data\n3..Exit")
        ch = int(input("\nEnter your choose: "))
        match(ch):
            case 1:
                sendData()
            case 2:
                readData()
            case 3:
                exit()    
