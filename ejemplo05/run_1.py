import requests
import json

# se lee el archivo json
with open('atp_tennis.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

base_datos = "personas005"
# se configura el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# envia los datos a la base de datos
response = requests.post(url, headers=headers, json=data)

# muestra respuestas
print(response.status_code)
print(response.json())