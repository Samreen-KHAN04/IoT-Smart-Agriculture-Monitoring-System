import pandas as pd
import random
from datetime import datetime, timedelta

rows = []

start_time = datetime(2026, 1, 1, 8, 0, 0)

for i in range(1000):

    timestamp = start_time + timedelta(minutes=i * 5)

    temperature = random.randint(20, 45)
    humidity = random.randint(35, 90)
    soil = random.randint(10, 100)
    light = random.randint(100, 1000)
    water = random.randint(10, 100)

    pump = "ON" if soil < 30 else "OFF"

    alert = "NORMAL"

    if soil < 30:
        alert = "LOW_SOIL_MOISTURE"

    if temperature > 40:
        alert = "HIGH_TEMPERATURE"

    if water < 20:
        alert = "LOW_WATER_LEVEL"

    rows.append([
        timestamp,
        temperature,
        humidity,
        soil,
        light,
        water,
        pump,
        alert
    ])

df = pd.DataFrame(rows, columns=[
    "Timestamp",
    "Temperature",
    "Humidity",
    "SoilMoisture",
    "LightIntensity",
    "WaterLevel",
    "PumpStatus",
    "Alert"
])

df.to_csv("sample_sensor_data.csv", index=False)

print("Dataset Created Successfully!")
print("Rows:", len(df))