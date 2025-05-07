import requests

url = 'http://192.168.1.15:5000'

respuesta = requests.get(url)

print("Respuesta del servidor:", respuesta.text)