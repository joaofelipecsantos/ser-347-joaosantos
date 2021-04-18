#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 05. Faça um programa em Python que pergunte ao usuário qual a série
que ele deseja calcular e em seguida imprima o nome da série escolhida.
"""

# Definindo as series
numero = list(range(0, 5, 1))
nomes = ['Lucas', 'Pell', 'Triangular', 'Square', 'Pentagonal']

# Informando as series disponíveis ao usuário
print('Veja as séries abaixo:\n0 Lucas\n1 Pell\n2 Triangular\n3 Square\n4 Pentagonal')

x = int(input('Digite o número correspondente à série você deseja computar: '))

if x not in numero:
    print(f'{x} não está na lista de series.')
else:
    serie = nomes[x]
    print(f"Você escolheu computar a série '{serie}'!")

# END
