#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 09. Escreva um programa em Python que avalie se dois segmentos de reta
se interceptam ou não.
"""

# Modules
import math

# Pontos para formar a reta (S)
print('Informe as coordenadas (x,y) de 2 pontos para formar um segmento de reta (S).\nUse vírgula para separar x e y.\nExemplo: 2.4,3.5')
ponto = input('Informe as coordenadas do Ponto 1 do segmento de reta S: ')
sx1 = float(ponto.split(',')[0])
sy1 = float(ponto.split(',')[1])
ponto = input('Informe as coordenadas do Ponto 2 do segmento de reta S: ')
sx2 = float(ponto.split(',')[0])
sy2 = float(ponto.split(',')[1])

print('Informe as coordenadas (x,y) de 2 pontos para formar um segmento de reta (T).\nUse vírgula para separar x e y.\nExemplo: 2.4,3.5')
ponto = input('Informe as coordenadas do Ponto 1 do segmento de reta T: ')
tx1 = float(ponto.split(',')[0])
ty1 = float(ponto.split(',')[1])
ponto = input('Informe as coordenadas do Ponto 2 do segmento de reta T: ')
tx2 = float(ponto.split(',')[0])
ty2 = float(ponto.split(',')[1])

# Verificar se os seg. de reta estão em locais em que possam haver interseção
# Definir x max e x min do segmento S
if sx1 > sx2:
    sxmax = sx1
    sxmin = sx2
else:
    sxmax = sx2
    sxmin = sx1
# Definir y max e y min do segmento S
if sy1 > sy2:
    symax = sy1
    symin = sy2
else:
    symax = sy2
    symin = sy1

# Definir a distancia P1 e P2 do segmento S até a reta T
denominador = math.sqrt((tx2 - tx1)**2 + (ty2 - ty1)**2)
hP1 = (((ty2 - ty1) * (sx1 - tx1)) - ((tx2 - tx1) * (sy1 - ty1))) / denominador
hP2 = (((ty2 - ty1) * (sx2 - tx1)) - ((tx2 - tx1) * (sy2 - ty1))) / denominador
# Definir a distancia P3 e P4 do segmento T até a reta S
denominador = math.sqrt((sx2 - sx1)**2 + (sy2 - sy1)**2)
hP3 = (((sy2 - sy1) * (tx1 - sx1)) - ((sx2 - sx1) * (ty1 - sy1))) / denominador
hP4 = (((sy2 - sy1) * (tx2 - sx1)) - ((sx2 - sx1) * (ty2 - sy1))) / denominador

# Avaliar se o seg. de reta T está fora dos limites de S (e vice-versa) para o eixo x
if (tx1 > sxmax) and (tx2 > sxmax):
    print('Os segmentos de reta não se interceptam.')
elif (tx1 < sxmin) and (tx2 < sxmin):
    print('Os segmentos de reta não se interceptam.')

# Avaliar se o seg. de reta T está fora dos limites de S (e vice-versa) para o eixo y
elif (ty1 > symax) and (ty2 > symax):
    print('Os segmentos de reta não se interceptam.')
elif (ty1 < symin) and (ty2 < symin):
    print('Os segmentos de reta não se interceptam.')

# Se os pontos hP1 e hP2 encontram-se em lados opostos do segmento T
# ou se os pontos hP3 e hP4 encontram-se em lados opostos do segmento S
# considerando que os seg. de reta S e T possuem ao menos um ponto em comum testado acima.
elif (hP1 * hP2 <= 0) or (hP3 * hP4 <= 0):  # Caso de apenas um ponto em comum incluído
    print('Os segmentos de reta se interceptam.')

# END