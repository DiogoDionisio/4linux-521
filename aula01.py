#!/usr/bin/python3
import requests
import json

response = requests.post('http://192.168.201.61/topicos',json={"titulo" : "BundaDoDiogo", "categoria" : "teste", "texto" : "lixo" })
print('Status: {0}'.format(response.status_code))
print(response.text)

response = requests.get('http://192.168.201.61/topicos')

topicos = response.json()
for topico in topicos:
    titulo = topico['titulo']
    data = topico['status']['visitas'][2]
    print('{0:.<50}{1}'.format(titulo, data))
