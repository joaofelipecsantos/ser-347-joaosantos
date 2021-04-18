#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
Lista-04
Exercício 01. Faça um programa para computar e apresentar a sequência de cada
uma das seguintes séries numéricas, depois de ler um número inteiro n ≥ 0:
"""

# Entrada
n = float(input('Digite um número inteiro ≥ 0: '))
# Confere se entrada é número inteiro positivo
n_round = round(n)
if (n - n_round) != 0 or n < 0:
    print('O número digitado é inválido.')
else:
    # Converte n para integer
    n = int(n)
    print(f'A sequência de cada uma das seguintes séries numéricas com n = {n} é:')
    # Lucas
    if n == 0:
        print('Série Lucas: 2')
    elif n == 1:
        print('Série Lucas: 2, 1')
    else:
        serie_list = [2, 1]
        count = 2 # Começa no 2 porque o n = 0 e n = 1 já estão na lista
        while count <= n:
            resultado = serie_list[-1] + serie_list[-2]
            serie_list.append(resultado)
            count+=1
        serie_str = str(serie_list)[1:-1]
        print(f'Série Lucas: {serie_str}')

    # Pell
    if n == 0:
        print('Série Pell: 0')
    elif n == 1:
        print('Série Pell: 0, 1')
    else:
        serie_list = [0, 1]
        count = 2 # Começa no 2 porque o n = 0 e n = 1 já estão na lista
        while count <= n:
            resultado = (2 * serie_list[-1]) + serie_list[-2]
            serie_list.append(resultado)
            count+=1
        serie_str = str(serie_list)[1:-1]
        print(f'Série Pell: {serie_str}')

    # Triangular
    serie_list = []
    count = 0
    while count <= n:
        resultado = int((count * (count + 1)) / 2)
        serie_list.append(resultado)
        count+=1
    serie_str = str(serie_list)[1:-1]
    print(f'Série Triangular: {serie_str}')

    # Square
    serie_list = []
    count = 0
    while count <= n:
        resultado = int(count ** 2)
        serie_list.append(resultado)
        count+=1
    serie_str = str(serie_list)[1:-1]
    print(f'Série Square: {serie_str}')

    # Pentagonal
    serie_list = []
    count = 0
    while count <= n:
        resultado = int((3 * (count ** 2) - count) / 2)
        serie_list.append(resultado)
        count+=1
    serie_str = str(serie_list)[1:-1]
    print(f'Série Pentagonal: {serie_str}')

# END