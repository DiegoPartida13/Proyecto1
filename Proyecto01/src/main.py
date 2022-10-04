"""
Archivo principal desde donde correremos nuestro proyecto
"""

import Ayuda_API as api
import webbrowser as web
import Creador_HTML as pagina
import cache as datos
import Lector as lectura

input = lectura.leer_archivo('docs/dataset1.csv')
cache = datos.Cache()
procesamiento_tickets = []

def main():
    """Procesamiento de tickets"""
    print("En breve se generara el documento...")
    for i in range(0,len(input)):
        entrada_tickets = input[i]
        despegue = (entrada_tickets[0], entrada_tickets[1], entrada_tickets[2])
        arribo = (entrada_tickets[3], entrada_tickets[4], entrada_tickets[5])
        clima_despegue = cache.obtenerValor(despegue[0])
        clima_arribo = cache.obtenerValor(arribo[0])
        if clima_arribo == None:
            clima_arribo = api.jsons(arribo[1], arribo[2])
            cache.agregarValor(arribo[0], clima_arribo)
        if clima_despegue == None:
            clima_despegue = api.jsons(despegue[1], despegue[2])
            cache.agregarValor(despegue[0], clima_despegue)
        ticket = (despegue[0], clima_despegue['main']['temp'], clima_despegue['weather'][0]['description'], arribo[0], clima_arribo['main']['temp'], clima_arribo['weather'][0]['description'])
        procesamiento_tickets.append(ticket)
        
    pagina.creador_HTML(procesamiento_tickets)
    web.open_new("docs/resultado.html")
    
if __name__ == "__main__":
    main()
    print("Los tickets se mostraran en un momento...")
