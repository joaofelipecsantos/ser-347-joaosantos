#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 03. Escreva um programa em Python que pergunte ao usuário um número
entre 0 e 10, e diga se ele é ímpar ou par.
"""


n = float(input('Escreva um número inteiro entre 0 e 10: '))

if n % 2 == 0 and (n >= 0 and n <= 10):
    print(f'O número {n} é par.')
elif n % 2 == 1 and (n >= 0 and n <= 10):
    print(f'O número {n} é ímpar.')
elif (n % 2 != 1) and (n % 2 != 0) and (n >= 0 and n <= 10):
    print(f'O número {n} não é inteiro.')
else:
    print(f'O número {n} não está entre 0 e 10.')

# END