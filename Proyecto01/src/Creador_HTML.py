"""
Creamos el html
"""
import pandas as panda

def creador_HTML(list): 
    """ crear el html 
    parametro list: procesamiento_tickets
    regresa el html con toda la información resultante
    """
    datos_salida = panda.DataFrame(list)     
    datos_nombres_columnas = datos_salida.set_axis(['|ORIGIN|','|TEMPERATURE ORIGIN|', '|CLOUD COVER ORIGIN|', '|DESTINATION|', '|TEMPERATURE DESTINATION|', '|CLOUD COVER DESTINATION|'], axis='columns') 
    datos_final = datos_nombres_columnas.style.set_caption("Los tickets han sido leidos correctamente")
    datos_mostrar = datos_final.to_html("docs/resultado.html")
    return datos_mostrar