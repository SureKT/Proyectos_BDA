import requests
import random
from datetime import datetime, timedelta
import time

# Configuración del Orion Context Broker
ORION_URL = "http://localhost:1026/v2/entities"

# Entidades a actualizar
SENSORS = [
    {"id": "SensorTemp_1", "attrs": ["temperatura", "humedad", "fechaRegistro"]},
    {"id": "SensorCO2_1", "attrs": ["co2", "fechaRegistro"]},
    {"id": "SensorCalidad_1", "attrs": ["temperatura", "ph", "cloro", "fechaRegistro"]}
]

# Fecha inicial (por ejemplo, 3 meses atrás)
start_date = datetime.now() - timedelta(days=90)
updates = 400

# Delay más alto para dar tiempo a QuantumLeap (en segundos)
DELAY = 2

for i in range(updates):
    sensor = SENSORS[i % len(SENSORS)]
    sensor_id = sensor["id"]

    # Fecha simulada (distribuida en 3 meses)
    simulated_date = start_date + timedelta(minutes=i * (90 * 24 * 60 / updates))
    date_str = simulated_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Generar datos realistas según tipo de sensor
    if sensor_id == "SensorTemp_1":
        temperatura = round(random.uniform(10, 35), 2)
        humedad = round(random.uniform(30, 90), 2)
        data = {
            "temperatura": {"value": temperatura},
            "humedad": {"value": humedad},
            "fechaRegistro": {"value": date_str}
        }
        
    elif sensor_id == "SensorCO2_1":
        co2 = round(random.uniform(400, 2000), 2)
        data = {
            "co2": {"value": co2},
            "fechaRegistro": {"value": date_str}
        }

    elif sensor_id == "SensorCalidad_1":
        temperatura = round(random.uniform(5, 30), 2)
        ph = round(random.uniform(6.5, 8.5), 2)
        cloro = round(random.uniform(0.2, 1.0), 2)
        data = {
            "temperatura": {"value": temperatura},
            "ph": {"value": ph},
            "cloro": {"value": cloro},
            "fechaRegistro": {"value": date_str}
        }

    # Enviar actualización a Orion
    response = requests.patch(
        f"{ORION_URL}/{sensor_id}/attrs",
        json=data,
        headers={"Content-Type": "application/json"}
    )

    print(f"[{i+1}/{updates}] Updated {sensor_id} at {date_str} -> {response.status_code}")

    # Pausa más larga para dar tiempo a QuantumLeap
    time.sleep(DELAY)