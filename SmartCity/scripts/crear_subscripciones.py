import requests
import json

ORION_URL = "http://localhost:1026/v2/subscriptions"
HEADERS = {"Content-Type": "application/json"}

subscripciones = [
    {
        "description": "Suscripción para SensorTemp_1",
        "subject": {
            "entities": [{"id": "SensorTemp_1", "type": "SensorTemperatura"}],
            "condition": {"attrs": ["temperatura", "humedad", "latitud", "longitud"]}
        },
        "notification": {
            "http": {"url": "http://quantumleap:8668/v2/notify"},
            "attrs": ["temperatura", "humedad", "fechaRegistro", "latitud", "longitud"]
        },
        "expires": "2040-01-01T14:00:00.00Z",
        "throttling": 5
    },
    {
        "description": "Suscripción para SensorCO2_1",
        "subject": {
            "entities": [{"id": "SensorCO2_1", "type": "SensorCO2"}],
            "condition": {"attrs": ["co2", "latitud", "longitud"]}
        },
        "notification": {
            "http": {"url": "http://quantumleap:8668/v2/notify"},
            "attrs": ["co2", "fechaRegistro", "latitud", "longitud"]
        },
        "expires": "2040-01-01T14:00:00.00Z",
        "throttling": 5
    },
    {
        "description": "Suscripción para SensorCalidad_1",
        "subject": {
            "entities": [{"id": "SensorCalidad_1", "type": "SensorCalidadAgua"}],
            "condition": {"attrs": ["temperatura", "ph", "cloro", "latitud", "longitud"]}
        },
        "notification": {
            "http": {"url": "http://quantumleap:8668/v2/notify"},
            "attrs": ["temperatura", "ph", "cloro", "fechaRegistro", "latitud", "longitud"]
        },
        "expires": "2040-01-01T14:00:00.00Z",
        "throttling": 5
    }
]

for sub in subscripciones:
    response = requests.post(ORION_URL, headers=HEADERS, data=json.dumps(sub))
    print(f"Creando suscripción '{sub['description']}': {response.status_code} {response.text}")
