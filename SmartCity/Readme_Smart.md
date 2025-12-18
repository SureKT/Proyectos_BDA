# SMART CITY

## Entidades OrionContextBroker

### Sensor Temperatura
{
  "id": "SensorTemp_1",
  "type": "SensorTemperatura",
  "fechaRegistro": {
    "type": "DateTime",
    "value": "2025-10-02T18:00:00-05:00"
  },
  "latitud": {
    "type": "Number",
    "value": -1.312315
  },
  "longitud": {
    "type": "Number",
    "value": 1.457488
  },
  "temperatura": {
    "type": "Number",
    "value": 25,
    "metadata": {
      "unidad": { "value": "Grados" }
    }
  },
  "humedad": {
    "type": "Number",
    "value": 80,
    "metadata": {
      "unidad": { "value": "Porcentaje" }
    }
  }
}

### Sensor CO2
{
  "id": "SensorCO2_1",
  "type": "SensorCO2",
  "fechaRegistro": {
    "type": "DateTime",
    "value": "2025-10-02T18:00:00-05:00"
  },
  "latitud": {
    "type": "Number",
    "value": -1.312315
  },
  "longitud": {
    "type": "Number",
    "value": 1.457488
  },
  "co2": {
    "type": "Number",
    "value": 88,
    "metadata": {
      "unidad": { "value": "ppm" }
    }
  }
}

### Sensor Calidad Agua
{
  "id": "SensorCalidad_1",
  "type": "SensorCalidadAgua",
  "fechaRegistro": {
    "type": "DateTime",
    "value": "2025-10-02T18:00:00-05:00"
  },
  "latitud": {
    "type": "Number",
    "value": -1.312315
  },
  "longitud": {
    "type": "Number",
    "value": 1.457488
  },
  "temperatura": {
    "type": "Number",
    "value": 25,
    "metadata": {
      "unidad": { "value": "Grados" }
    }
  },
  "ph": {
    "type": "Number",
    "value": 80,
    "metadata": {
      "unidad": { "value": "Porcentaje" }
    }
  },
  "cloro": {
    "type": "Number",
    "value": 80,
    "metadata": {
      "unidad": { "value": "mgL" }
    }
  }
}

## Subscripciones para QuantumLeam

### Sensor Temperatura
{
    "description": "Suscripción para monitorear SensorTemp_1",
    "subject": {
        "entities": [
            {
                "id": "SensorTemp_1",
                "type": "SensorTemperatura"
            }
        ],
        "condition": {
            "attrs": [
                "fechaRegistro",
                "humedad",
                "latitud",
                "longitud",
                "temperatura"
            ]
        }
    },
    "notification": {
        "http": {
            "url": "http://quantumleap:8668/v2/notify"
        },
        "attrs": [
            "fechaRegistro",
            "humedad",
            "latitud",
            "longitud",
            "temperatura"
        ]
    },
    "expires": "2040-01-01T14:00:00.00Z",
    "throttling": 5
}

### Sensor CO2
{
    "description": "Suscripción para monitorear SensorCO2_1",
    "subject": {
        "entities": [
            {
                "id": "SensorCO2_1",
                "type": "SensorCO2"
            }
        ],
        "condition": {
            "attrs": [
                "fechaRegistro",
                "co2",
                "latitud",
                "longitud"
            ]
        }
    },
    "notification": {
        "http": {
            "url": "http://quantumleap:8668/v2/notify"
        },
        "attrs": [
            "fechaRegistro",
            "co2",
            "latitud",
            "longitud"
        ]
    },
    "expires": "2040-01-01T14:00:00.00Z",
    "throttling": 5
}

### Sensor Calidad Agua
{
    "description": "Suscripción para monitorear SensorCalidad_1",
    "subject": {
        "entities": [
            {
                "id": "SensorCalidad_1",
                "type": "SensorCalidadAgua"
            }
        ],
        "condition": {
            "attrs": [
                "fechaRegistro",
                "Cloro",
                "latitud",
                "longitud",
                "ph",
                "temperatura"
            ]
        }
    },
    "notification": {
        "http": {
            "url": "http://quantumleap:8668/v2/notify"
        },
        "attrs": [
            "fechaRegistro",
            "Cloro",
            "latitud",
            "longitud",
            "ph",
            "temperatura"
        ]
    },
    "expires": "2040-01-01T14:00:00.00Z",
    "throttling": 5
}