"""
Pruebas unitarias de Ayuda_API.py
"""
import unittest #Realizar pruebas unitarias
import sys
sys.path.append('src')
from Ayuda_API import solicitud
from Ayuda_API import jsons

class Ayuda_API(unittest.TestCase):
    """unittest.TestCase"""
    def test_solicitud(self):
        """test para ejecuciones"""
        resultado = solicitud("25.7785","-100.107") 
        assert resultado.status_code== 200

    def test_jsons(self):
        """test para verificaciones"""
        nombreCiudad = jsons("25.7785","-100.107")['name'] 
        nombrePais = jsons("25.7785","-100.107")['sys']['country'] 
        print("nombre de ciudad:%s, nombre de pais: %s" , nombreCiudad, nombrePais)
        assert  nombreCiudad == 'Monterrey' and nombrePais == 'MX'

if __name__ == '__main__':
    unittest.main()