'''
Universidad Sergio Arboleda
Autores: Juan Pablo Mora Aragón
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:Juan.mora03@gmail.com
'''
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize('Cy_functionE.pyx'))

setup(ext_modules=exts)