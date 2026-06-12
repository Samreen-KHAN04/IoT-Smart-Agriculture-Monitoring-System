

# IoT Smart Agriculture Monitoring System

## Overview

The IoT Smart Agriculture Monitoring System is a simulation-based smart farming solution designed to monitor environmental conditions and assist in irrigation management. The system collects sensor readings such as temperature, humidity, soil moisture, light intensity, and water level, analyzes the data, generates alerts, and provides recommendations through an interactive dashboard.

---

## Problem Statement

Traditional agricultural monitoring often depends on manual observation, resulting in inefficient water usage and delayed responses to environmental changes. An automated monitoring solution can help improve resource utilization and crop productivity.

---

## Objectives

* Monitor environmental parameters in agricultural fields.
* Track soil moisture for irrigation management.
* Monitor water reservoir levels.
* Generate alerts for abnormal conditions.
* Automate irrigation recommendations.
* Visualize sensor data through dashboards.

---

## System Architecture

```text
Sensors
(Temperature, Humidity, Soil Moisture,
Light Intensity, Water Level)

        ↓

Data Collection Layer
(simulator.py)

        ↓

CSV Storage
(sensor_data.csv)

        ↓

Analytics & Alert Engine
(alerts.py)

        ↓

Decision Logic
(Pump ON/OFF)

        ↓

Streamlit Dashboard

        ↓

Farmer / User
```

---

## Hardware Components

| Component            | Purpose                           |
| -------------------- | --------------------------------- |
| ESP32 DevKit V1      | Main Controller                   |
| DHT22                | Temperature & Humidity Monitoring |
| Photoresistor (LDR)  | Light Monitoring                  |
| Soil Moisture Sensor | Soil Condition Monitoring         |
| Water Level Sensor   | Water Reservoir Monitoring        |
| Relay Module         | Pump Control                      |
| Water Pump           | Irrigation System                 |

---

## Software Components

* Python
* Streamlit
* Pandas
* Plotly
* Arduino IDE
* Wokwi Simulator

---

## Dataset Description

The dataset contains simulated agricultural sensor readings.

| Attribute    | Description       |
| ------------ | ----------------- |
| Time         | Timestamp         |
| Temperature  | Temperature (°C)  |
| Humidity     | Humidity (%)      |
| SoilMoisture | Soil Moisture (%) |
| Light        | Light Intensity   |
| WaterLevel   | Water Level (%)   |
| Pump         | ON/OFF Status     |
| Alert        | Generated Alert   |

---

## Methodology

1. Generate simulated sensor readings.
2. Store readings in CSV format.
3. Analyze sensor values.
4. Generate alerts using threshold logic.
5. Trigger irrigation recommendations.
6. Visualize data through the dashboard.

---

## Dashboard Features

### System Overview

Displays current sensor readings.

### Farm Health Status

Shows overall environmental condition.

### Irrigation Recommendation

Suggests irrigation actions based on soil moisture levels.

### Alert History

Displays alert frequency and trends.

### Pump Activity Summary

Shows irrigation system usage statistics.

### Trend Analysis

Visualizes historical sensor readings.

---

## Results

The system successfully:

* Simulates IoT sensor readings.
* Monitors environmental conditions.
* Detects abnormal events.
* Generates alerts automatically.
* Provides irrigation recommendations.
* Visualizes sensor data through interactive charts.

---

## Future Scope

* Real sensor integration.
* MQTT communication.
* Cloud-based monitoring.
* Mobile application development.
* Machine learning-based irrigation prediction.
* Weather API integration.
* Remote pump control.

---

## Conclusion

The IoT Smart Agriculture Monitoring System demonstrates the application of IoT concepts in modern agriculture. By combining sensor monitoring, data analytics, automation logic, and visualization, the system provides a foundation for intelligent farming solutions.

---

## References

1. ESP32 Documentation
2. Arduino Documentation
3. Streamlit Documentation
4. Pandas Documentation
5. Plotly Documentation
6. IoT Smart Agriculture Research Papers

---

## Acknowledgement

Special thanks to my mentor for continuous guidance, support, and encouragement throughout the development of this project.

Then commit and push:

```powershell
git add docs/project_report.md
git commit -m "Added project documentation"
git push origin main
```

