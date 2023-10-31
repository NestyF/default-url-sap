# Default-url-sap
Este script es una herramienta que permite a los usuarios verificar la disponibilidad de una lista de URLs almacenadas en un archivo de texto. Funciona de la siguiente manera:
*El usuario proporciona la ruta del archivo de texto que contiene las URLs que se desean verificar. <br>
*El script lee las URLs desde el archivo, verifica cada una de ellas realizando solicitudes HTTP GET y comprueba el código de respuesta de cada solicitud.<br>
*Para las URL que responden con un código de respuesta 200 (indicando una respuesta exitosa), el script las muestra en color verde, indicando que funcionan correctamente.<br>
*Para las URL que no responden con un código de respuesta 200 o que generan errores durante la solicitud, el script las muestra en rojo, indicando problemas de disponibilidad.<br>


# Uso
Usar el Script es bastante facil, despues de descargado lo ejecutamos de la siguiente manera: <br>
python sap_request.py

![image](https://github.com/NestyF/default-url-sap/assets/31319663/37d72288-4171-42b8-b316-abe1dd108cde)

# Resumen Final
Al final de la ejecución, el script presenta un resumen que incluye las URLs que funcionaron correctamente, destacándolas en verde, lo que facilita la identificación de las URL en buen estado en la lista verificada. <br>
![image](https://github.com/NestyF/default-url-sap/assets/31319663/5f73276a-30bd-4332-a1f6-0fad8747080e)
