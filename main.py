#Importar librerías
import numpy as np
# Importar módulos
import compresor
import descompresor
import verificador

# Archivo de entrada
input_file = input('Ingrese el nombre del archivo con su extensión: ')

# Llamar a la función de compresión
compresor.compress(input_file)

# Llamar a la función de descompresión
descompresor.decompress('comprimido.elmejorprofesor')

# Llamar a la función de verificación
verificador.verify(input_file,'descomprimido-elmejorprofesor.txt')