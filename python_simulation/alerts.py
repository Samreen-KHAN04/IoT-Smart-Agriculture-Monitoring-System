def generate_alert(temp, soil, water):

    alerts = []

    if soil < 30:
        alerts.append("LOW SOIL MOISTURE")

    if temp > 40:
        alerts.append("HIGH TEMPERATURE")

    if water < 20:
        alerts.append("LOW WATER LEVEL")

    if len(alerts) == 0:
        alerts.append("NORMAL")

    return alerts