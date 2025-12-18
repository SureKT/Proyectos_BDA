import requests
import json

ORION_URL = "http://localhost:1026/v2/entities"
HEADERS = {"Content-Type": "application/json"}

entidades = [
    {
        "id": "SensorTemp_1",
        "type": "SensorTemperatura",
        "fechaRegistro": {"type": "DateTime", "value": "2025-10-02T18:00:00-05:00"},
        "latitud": {"type": "Number", "value": -1.312315},
        "longitud": {"type": "Number", "value": 1.457488},
        "temperatura": {"type": "Number", "value": 25, "metadata": {"unidad": {"value": "Grados"}}},
        "humedad": {"type": "Number", "value": 80, "metadata": {"unidad": {"value": "Porcentaje"}}}
    },
    {
        "id": "SensorCO2_1",
        "type": "SensorCO2",
        "fechaRegistro": {"type": "DateTime", "value": "2025-10-02T18:00:00-05:00"},
        "latitud": {"type": "Number", "value": -1.312315},
        "longitud": {"type": "Number", "value": 1.457488},
        "co2": {"type": "Number", "value": 88, "metadata": {"unidad": {"value": "ppm"}}}
    },
    {
        "id": "SensorCalidad_1",
        "type": "SensorCalidadAgua",
        "fechaRegistro": {"type": "DateTime", "value": "2025-10-02T18:00:00-05:00"},
        "latitud": {"type": "Number", "value": -1.312315},
        "longitud": {"type": "Number", "value": 1.457488},
        "temperatura": {"type": "Number", "value": 25, "metadata": {"unidad": {"value": "Grados"}}},
        "ph": {"type": "Number", "value": 80, "metadata": {"unidad": {"value": "Porcentaje"}}},
        "cloro": {"type": "Number", "value": 80, "metadata": {"unidad": {"value": "mgL"}}}
    }
]

for entidad in entidades:
    response = requests.post(ORION_URL, headers=HEADERS, data=json.dumps(entidad))
    print(f"Creando {entidad['id']}: {response.status_code} {response.text}")
