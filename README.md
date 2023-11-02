# Descripción

Este script verifica la disponibilidad de URLs proporcionadas por el usuario y muestra el resultado en colores (esta pensado especificamente para verificar URLS por defecto y con información sencible de SAP)

## Funcionalidad

- El usuario proporciona la ruta del archivo de texto que contiene las URLs que se desean verificar.
- El script lee las URLs desde el archivo, verifica cada una de ellas realizando solicitudes HTTP GET y comprueba el código de respuesta de cada solicitud.
- Para las URL que responden con un código de respuesta 200 (indicando una respuesta exitosa), el script las muestra en color verde, indicando que funcionan correctamente.
- Para las URL que no responden con un código de respuesta 200 o que generan errores durante la solicitud, el script las muestra en rojo, indicando problemas de disponibilidad.

## Uso

1. Ejecuta el script y proporciona la ruta del archivo de texto que contiene las URLs que deseas verificar.
2. El script verificará cada URL y mostrará los resultados en la consola.

![image](https://github.com/NestyF/default-url-sap/assets/31319663/0635c246-0572-4bf9-b500-0c7654830f71)

## Resumen Final

Al final de la ejecución, el script presenta un resumen que incluye las URLs que funcionaron correctamente, destacándolas en verde, lo que facilita la identificación de las URL en buen estado en la lista verificada.

![image](https://github.com/NestyF/default-url-sap/assets/31319663/5f73276a-30bd-4332-a1f6-0fad8747080e)

## Requisitos

- Python 3.x
- Paquete `requests` (instálalo con `pip install requests`)
- Paquete `termcolor` (instálalo con `pip install termcolor`)





