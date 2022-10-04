"""
Obtención de información con las llamadas al API
"""
import requests #Libreria para solicitudes
from dotenv import load_dotenv #descarga libreria env
import os #Permite acceder a funcionalidades dependientes del sistema operativo

load_dotenv()  #en un archivo .env se crearan las variabes de entorno 
API_KEY = os.getenv("API_KEY")

def solicitud(lat,lon):
    """ método: Devuelve la respuesta del api
        parametro lat: Representa el valor de la latitud de la ciudad
        parametro lon: Representa el valor de la longitud de la ciudad
        regresa respuesta: La respuesta del API, tiene que ser 200 para estar correcto
    """
    respuesta = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={API_KEY}&lang=sp&units=metric")
    return respuesta 
def jsons(lat,lon):
    """ metodo: Devuelve el json del request
        parametro lat: Representa el valor de la latitud de la ciudad
        parametro lon: Representa el valor de la longitud de la ciudad
        regresa respuesta: Json con los datos 
    """
    respuesta = solicitud(lat,lon)
    return respuesta.json()
