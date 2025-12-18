import requests
import json
from random import randint, uniform

ORION_URL = "http://localhost:1026/v2/entities"
HEADERS = {"Content-Type": "application/json"}

# Simulación de actualización de valores
actualizaciones = {
    "SensorTemp_1": {
        "temperatura": {"value": round(uniform(20, 30), 2)},
        "humedad": {"value": randint(40, 90)}
    },
    "SensorCO2_1": {
        "co2": {"value": randint(50, 150)}
    },
    "SensorCalidad_1": {
        "temperatura": {"value": round(uniform(20, 28), 2)},
        "ph": {"value": round(uniform(6.5, 8.5), 2)},
        "cloro": {"value": round(uniform(0.5, 2.0), 2)}
    }
}

for entidad_id, data in actualizaciones.items():
    url = f"{ORION_URL}/{entidad_id}/attrs"
    response = requests.patch(url, headers=HEADERS, data=json.dumps(data))
    print(f"Actualizando {entidad_id}: {response.status_code} {response.text}")
