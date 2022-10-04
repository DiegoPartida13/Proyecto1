"""
Los datos consultados anteriormente por la API se guardan
"""
class Cache:
    def __init__(self):
        """Inicia un nuevo guardado de Cache"""
        self.guardado = {}

    def obtenerValor(self, info_aerea):
        """ valor de 'info_aerea' dentro del cache
        ValueError: En caso de que "info_aerea" tenga un numero diferente a 3 caracteres o no sea un str, se lanzara esta excepcion
        """
        if type(info_aerea) != str and len(info_aerea) != 3:
            raise ValueError
        return self.guardado.get(info_aerea)
    
    def agregarValor(self, info_aerea, info):
        """agrega valores al cache"""
        if type(info_aerea) != str or type(info) != dict:
            raise TypeError
        if len(info_aerea) != 3 :
            raise ValueError
        self.guardado.update({info_aerea: info})
        
    def cacheActualizacion(self, nuevo):
        """Se realizara una nueva actualizacion del cache
            parametro nuevo: es el cache del que tomaremos los nuevos datos 
        """
        if type(nuevo) != dict:
            raise TypeError
        self.guardado.update(nuevo)

    def obtencion(self):
        """Lista del cache de "info_aerea"
        """
        return self.guardado.keys()

    def longitud(self):
        """regresa la longitud del cache"""
        return len(self.guardado)

    def limpiar(self): 
        """Borra todo el cache"""
        self.guardado.clear()