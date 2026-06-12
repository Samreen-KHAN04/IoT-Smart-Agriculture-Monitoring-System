import random
import pandas as pd
from datetime import datetime
import time
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILE = os.path.join(BASE_DIR, "data", "sensor_data.csv")

os.makedirs(os.path.dirname(FILE), exist_ok=True)

while True:

    temperature = random.randint(20, 45)
    humidity = random.randint(35, 90)
    soil = random.randint(10, 100)
    light = random.randint(100, 1000)
    water = random.randint(10, 100)

    pump = "ON" if soil < 30 else "OFF"

    alert = "NORMAL"

    if soil < 30:
        alert = "LOW SOIL MOISTURE"

    if temperature > 40:
        alert = "HIGH TEMPERATURE"

    if water < 20:
        alert = "LOW WATER LEVEL"

    row = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Temperature": temperature,
        "Humidity": humidity,
        "SoilMoisture": soil,
        "Light": light,
        "WaterLevel": water,
        "Pump": pump,
        "Alert": alert
    }

    df = pd.DataFrame([row])

    try:
        old = pd.read_csv(FILE)
        df = pd.concat([old, df], ignore_index=True)
    except:
        pass

    df.to_csv(FILE, index=False)

    print("=" * 50)
    print(row)

    time.sleep(5)