#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: SER-347 - João Santos

LISTA - 02
EXERCÍCIO 04
"""

# importar a biblioteca math
import math

# Informação de texto
print('\nInforme as coordenadas (latitude e longitude), em GRAU-DECIMAL,\nde dois pontos quaisquer na esfera terrestre.')

# Interacao com usuario
lat1 = float(input('Latitude do Ponto 1: '))
lon1 = float(input('Longitude do Ponto 1: '))

lat2 = float(input('Latitude do Ponto 2: '))
lon2 = float(input('Longitude do Ponto 2: '))

# Informando valores as variaveis
phi1 = math.radians(lat1)  # phi = latitude em radianos
lambda1 = math.radians(lon1)  # lambda = longitude em radianos
phi2 = math.radians(lat2)
lambda2 = math.radians(lon2)

r = 6371  # r: é o raio da esfera (∼6371km)

# Montando a equacao
# Primeiro termo dentro da raiz
primeiro = math.sin((phi2 - phi1) / 2)**2
# Segundo termo dentro da raiz
segundo = math.cos(phi1) * math.cos(phi2) * (math.sin((lambda2 - lambda1) / 2)**2)
# Raiz quadrada do primeiro termo + segundo termo
raiz = math.sqrt(primeiro + segundo)
# Resultado da distancia
d = 2 * r * math.asin(raiz)

# Resultado
print('As coordenadas estão', round(d, ndigits=2), 'km de distância.')

# END