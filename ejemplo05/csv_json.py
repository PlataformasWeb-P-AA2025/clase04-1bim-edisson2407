import json
import csv

# se lee el archivo csv
with open('atp_tennis.csv', mode='r', encoding='ISO-8859-1') as archivo_csv:
	# transforma el csv en una lista de diccionarios
	lectura_csv = csv.DictReader(archivo_csv)
	# crea una lista de diccionarios
	lista = []
	for r in lectura_csv:
		lista.append(r)

# se crea un diccionario con la lista de diccionarios
diccionario = {"docs": lista}

# se crea el archivo json
with open('atp_tennis.json', mode='w', encoding='utf-8') as archivo_json:
	json.dump(diccionario, archivo_json, indent=4)

print('Script finalizado.')