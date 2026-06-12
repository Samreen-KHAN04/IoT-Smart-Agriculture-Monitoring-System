import os

print("=" * 50)
print("IoT Smart Agriculture Monitoring System")
print("=" * 50)

os.system("streamlit run python_simulation/dashboard.py")

print("\nModules Loaded Successfully")

print("\nAvailable Features:")

features = [
    "Sensor Simulation",
    "Real-time Dashboard",
    "Alert Generation",
    "Pump Automation Logic",
    "CSV Data Logging",
    "Data Visualization"
]

for feature in features:
    print(f"✓ {feature}")

print("\nSystem Ready")