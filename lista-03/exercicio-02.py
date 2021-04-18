#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 02. Escreva um programa em Python que leia o tamanho dos lados de um
triângulo, avalie se esses valores realmente formam um triângulo, e em caso positivo,
classifique o triângulo em isósceles, escaleno ou equilátero.
"""

# Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
# um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
# e menor que a soma dos outros dois lados.

print('Informe a medida dos três segmentos de reta do triângulo.')

a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if a < 0 or b < 0 or c < 0:
    print('Os valores devem ser números reais positivos.')
elif (a < (b + c) and b < (a + c) and c < (a + b)) and (a > abs(b - c) and b > abs(a - c) and c > abs(b - a)):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print(f'Os segmentos de reta {a}, {b} e {c} formam um triângulo isósceles.')
    elif a == b and a == c:
        print(f'Os segmentos de reta {a}, {b} e {c} formam um triângulo equilátero.')
    else:
        print(f'Os segmentos de reta {a}, {b} e {c} formam um triângulo escaleno.')
else:
    print(f'Os segmentos de reta {a}, {b} e {c} não formam um triângulo.')

# END