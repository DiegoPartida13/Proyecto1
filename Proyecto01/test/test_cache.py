"""
Corre las pruebas unitarias necesarias para comprobar la correcta implementacion de 'cache.py'

"""
import unittest #Hacer pruebas unitarias
import sys
sys.path.append('src')
import cache

class TestCache(unittest.TestCase):
    def test_agregarValor(self):
        cache_ejemplo = cache.Cache()
        try:
            cache_ejemplo.agregarValor("MTY",{'Country': 'Mexico', 'City': 'Monterrey', 'Elevation': 390}) #debería de ser aceptado
        except Exception: 
            raise  AssertionError
        else: 
            self.assertTrue(cache_ejemplo.longitud() == 1)
        try:
            cache_ejemplo.agregarValor("diso",{'Country': 'Mexico', 'City': 'Monterrey', 'Elevation': 390}) #No debe de ser aceptado
        except ValueError:
            pass
        else:
            self.assertFalse(cache_ejemplo.longitud() == 2)
        try:
            cache_ejemplo.agregarValor("mty", "dor")
        except TypeError:
            pass
        else:
            self.assertFalse(cache_ejemplo.longitud() == 2)
        try: 
            cache_ejemplo.agregarValor("MAD", {'Country': 'España', 'City': 'Madrid', 'Elevation':610}) #Debería de ser aceptado
        except Exception:
            raise AssertionError
        else:
            self.assertTrue(cache_ejemplo.longitud() == 2)

    def test_CacheActualizacion(self):
        cache_ejemplo2 = cache.Cache()
        try:
            cache_ejemplo2.cacheActualizacion("Bul") #No debería de ser aceptado
        except TypeError:
            pass
        else:
            raise AssertionError
        try:
            cache_ejemplo2.cacheActualizacion(Example.cache1.copy())
        except Exception:
            raise AssertionError
        self.assertTrue(cache_ejemplo2.longitud() == 5)

    def test_limpiar(self):
        cache_ejemplo3 = cache.Cache()
        cache_ejemplo3.cacheActualizacion(Example.cache1.copy())
        cache_ejemplo3.limpiar()
        self.assertTrue(cache_ejemplo3.longitud() == 0)

class Example:
    cache1 = {
        'MTY': {'Country': 'Mexico', 'City': 'Monterrey', 'Elevation': 390}, 
        'MAD': {'Country': 'España', 'City': 'Madrid', 'Elevation':610},
        'SCL': {'Country': 'Chile', 'City': 'Santiago de Chile', 'Elevation': 474}
    }

if __name__ == '__main__':
    unittest.main()
    