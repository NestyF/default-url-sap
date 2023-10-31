import requests
from termcolor import colored

# Solicitar la ruta del archivo de texto al usuario
ruta_archivo = input(colored("Introduce la ruta del archivo de texto que contiene las URLs: ", "blue"))

# Obtener la lista de URLs del archivo de texto
with open(ruta_archivo, "r") as file:
    urls = file.readlines()
    urls = [url.strip() for url in urls]

# Crear una lista para almacenar las URL que funcionaron correctamente
urls_correctas = []

# Verificar cada URL en la lista
for url in urls:
    try:
        # Enviar una solicitud HTTP GET a la URL
        response = requests.get(url)
        # Comprobar el código de respuesta HTTP
        if response.status_code == 200:
            print(colored(f"La URL {url} funciona correctamente.", "green"))
            # Agregar la URL a la lista de URL correctas
            urls_correctas.append(url)
        else:
            print(colored(f"La URL {url} no funciona correctamente.", "red"))
    except requests.exceptions.RequestException:
        print(colored(f"No se puede acceder a la URL {url}.", "red"))

# Mostrar un resumen al final con las URL que funcionaron correctamente
print("\nResumen de URLS que funcionaron correctamente:")
for url in urls_correctas:
    print(colored(url, "green"))
