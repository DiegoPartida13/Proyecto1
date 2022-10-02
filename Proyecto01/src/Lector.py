"""Leeremos nuestra base de datos usando la libreria de Pandas
"""

import pandas as panda

def leer_archivo(data): 
    """ lectura del archivo csv 
        parametro data: es el archivo csv
        regresa lista: Lista de Strings del archivo csv
    """
    try:
        datos = panda.read_csv(data)
        
        datos_coodenadas = datos[['origin','origin_latitude','origin_longitude', 'destination', 'destination_latitude','destination_longitude']]
        
        input = datos_coodenadas.values.tolist() 
    except panda.errors.EmptyDataError:
        print("No se encuentran datos")
    except panda.errors.ParserError:
        print("Error parse")
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception:
        print("Se ha encontrado una excepcion")
    return input