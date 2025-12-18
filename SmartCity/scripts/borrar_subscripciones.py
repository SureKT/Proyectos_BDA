# delete_subscriptions.py
import requests

ORION_URL = "http://localhost:1026/v2/subscriptions"

# Obtener todas las suscripciones actuales
response = requests.get(ORION_URL)
if response.status_code != 200:
    print(f"❌ Error al obtener suscripciones: {response.status_code} {response.text}")
    exit()

subscriptions = response.json()

if not subscriptions:
    print("ℹ️ No hay suscripciones que eliminar.")
    exit()

# Eliminar cada suscripción por ID
for sub in subscriptions:
    sub_id = sub.get("id")
    if sub_id:
        del_response = requests.delete(f"{ORION_URL}/{sub_id}")
        if del_response.status_code in [204, 404]:
            print(f"✅ Eliminada suscripción con ID: {sub_id}")
        else:
            print(f"⚠️ Error al eliminar {sub_id}: {del_response.status_code} {del_response.text}")

print("🧹 Proceso de limpieza de suscripciones completado.")
