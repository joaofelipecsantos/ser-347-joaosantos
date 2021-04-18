#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 08. Escreva um programa que calcule a menor distância entre um ponto
e uma reta, possibilitando que o usuário entre com as informações de dois pontos
pertencentes à reta, bem como o ponto para o qual deva ser avaliada a distância.
"""

# Modules
import math

# Pontos para formar a reta (r)
print('Informe as coordenadas (x,y) de 2 pontos para formar uma reta (r).\nUse vírgula para separar x e y.\nExemplo: 2.4,3.5')
ponto = input('Informe as coordenadas do Ponto 1: ')
x1 = float(ponto.split(',')[0])
y1 = float(ponto.split(',')[1])

ponto = input('Informe as coordenadas do Ponto 2: ')
x2 = float(ponto.split(',')[0])
y2 = float(ponto.split(',')[1])

# Ponto P no plano da reta (r)
# A distância de P=(x,y) a r é dada por |h(x,y)|.
print('\nInforme as coordenadas (x,y) do ponto P.\nUse vírgula para separar x e y.\nExemplo: 2.4,3.5')
ponto = input('Informe as coordenadas do Ponto P: ')
px = float(ponto.split(',')[0])
py = float(ponto.split(',')[1])

# Condição de existência
denominador = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
if  denominador > 0:
    h = (((y2 - y1) * (px - x1)) - ((x2 - x1) * (py - y1))) / denominador
    print('A menor distância entre o ponto P e a reta r é', abs(h), '.')
else: # P1 = P2 na equação da reta
    print('Não é possível calcular a distância do ponto P à reta r com as coordenadas (x,y) informadas.')

# END