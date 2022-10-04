Proyecto 1

### Integrantes

-  Olivares García Sarah Sophía   / Usurario: Sophia-Olivares   / Nro.Cuenta 318360638
-  Partida Pérez Diego Iván       / Usuario: DiegoPartida13    / Nro.Cuenta 318368098

## Aclaraciones sobre el método de trabajo del equipo

Trabajamos conjuntamente en videollamadas, analizando el proyecto, discutiendo soluciones, pensando conjuntamente y llegando a una resolución.
Los 2 trabajamos en todos los archivos en videollamada, es decir, en ocasiones Diego programaba mientras estaba en videollamada con Sophía (y viceversa)apoyándose y tomando desiciones sobre el proyecto de manera sincrona.
Al final, cada quien subió lo que programó del proyecto durante las videollamadas.

## Instrucciones:

1. *Instalar python (version 3+)*
entramos a la página oficial: https://www.python.org/downloads/
Descargamos python y seguimos instrucciones.

Verificamos que se realizara la descarga correctamente con el siguiente comando en terminal:

python3 --version

2. *instalar pandas*
En terminal, el siguiente comando:

pip install pandas

3. *instalar Jupyter Notebook*
En terminal, el siguiente comando:

pip install jupyterlab

4. *requests en python*
En terminal escribimos el siguiente comando para instalar: 

python -m pip install requests

5. *Instalar python-dotenv.* 
Ocultaremos información en un archivo .env, que será la APi key.
Escribimos el siguiente comando en la terminal:

pip install python-dotenv

6. *API KEY*
Entraremos a Open Weather en el siguiente enlace: https://openweathermap.org/api
Creamos una cuenta y obtenemos una API key
Sustituiremos la key obtenida en el archivo ".env", justo en "keysustitucion" después de "=" 

7. *miniconda* 
Instalamos miniconda, la cual es un instalador minimo gratuito. Una pequeña versión de Anaconda.
Entramos a la siguiente página: 
https://docs.conda.io/en/latest/miniconda.html

Instalamos dependiendo de nuestro sistema operativo.

8. *Instalar VS Code*
Entramos a la siguiente URL:
https://code.visualstudio.com/
Instalamos para nuestro sistema operativo y seguimos la serie de pasos que nos indica el instalador.

## Obtención de resultados (opcion 1)
1.  En la terminal, dirigete al directorio de Proyecto1 y correr el siguiente comando:
python3 src/main.py

2. Se procesan los tickets y se generará un documento resultado.html en el directorio docs, posteriormente se abrirá el documento en tu navegador

## Obtención de resultados (opcion 2)
1. En Visual Studio Code, abrimos la carpeta completa de _Proyecto01_

2. Nos posicionamos en _src_ y después en el main.py 

3. Le damos en "Run Code"

4.- Esperamos a la ejecución y obtendremos los resultados! :3

## Instrucciones para correr pruebas:
En la terminal dirigete a Proyecto01 y coloca la siguiente linea de comando:
pytest