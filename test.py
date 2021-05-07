'''
Universidad Sergio Arboleda
Autores: Juan Pablo Mora Aragón
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:Juan.mora03@gmail.com
'''
from functionE import rbf_network
from Cy_functionE import Cy_rbf_network
import numpy as np
import time

### Inicializar
D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10


### Tiempos
inicio = time.time()
rbf_network(X, beta, theta)
tiempoPy = time.time() - inicio

inicio = time.time()
Cy_rbf_network(X, beta, theta)
tiempoCy = time.time() - inicio

speedUp = round(tiempoPy/tiempoCy,3)

print("Time Python: {} \n".format(tiempoPy))
print("Time Cython: {} \n".format(tiempoCy))
print("SpeedUp: {} \n".format(speedUp))