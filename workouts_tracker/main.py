

import requests
from datetime import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

APLIKATION_ID = os.getenv('NT_AP_ID')
API_KEY = os.getenv('NT_API_KEY')

USER_NAME = os.getenv('NAME')
PASSWORD = os.getenv('PASSW')

GENDER = "Male"
WEIGHT_KG = "76"
HEIGHT_CM = "178"
AGE = "34"

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("sheet")

# введений текст з вправами
text = input("Tell me which exercises you did ")

data = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# параметри запиту
payload = {
    "query": text
}

# заголовки запиту
headers = {
    "Content-Type": "application/json",
    "x-app-id": APLIKATION_ID,
    "x-app-key": API_KEY,
}

# виконуємо запит до API
response = requests.post(url, json=data, headers=headers)

# отримуємо результат у форматі JSON
result = response.json()
print(result)

today_date = datetime.now().strftime("%d-%m-%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    shit_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint,
                                   json=shit_input,
                                   auth=(USER_NAME, PASSWORD)
                                   )
    print(sheet_response.text)
