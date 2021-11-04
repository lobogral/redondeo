# Redondeo
Redondeo mitad arriba en Python.

La forma estándar de redondear números en Python es confusa, por eso este paquete ofrece la forma de 
redondear más usual, para el último decimal o la última unidad:

1. Menor a 5 redondea a 0.
2. Mayor o igual a 5 redondea a 1.

## Instalación

Para instalar la versión más reciente de ``redondeo`` usando pip:

1. Descargar el archivo .tar.gz mediante el siguiente [link](https://github.com/lobogral/redondeo/releases/latest/download/redondeo.tar.gz).

2. Ejecutar el comando:

        $ pip install redondeo.tar.gz

Si se desea instalar para desarrollo, ejecutar lo siguiente:

    $ git clone https://github.com/lobogral/redondeo.git
    $ cd redondeo
    $ pip install -e .
    
## Ejemplo

Solo es necesario ejecutar Python y escribir lo siguiente:

``` python
>>> from redondeo.redondeo import redondear
>>> print(redondear(4.5678, 3))
4.568
```

## Referencias

* https://stackoverflow.com/questions/33019698/how-to-properly-round-up-half-float-numbers
