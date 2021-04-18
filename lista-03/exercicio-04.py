#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 04. Escreva um programa em Python que pergunte ao usuário um número qualquer (> 0),
e diga se ele é divisível apenas por 2, apenas por 3, por 2 e por 3,
ou se não é divisível nem por 2 nem por 3.
"""

n = float(input('Escreva um número maior que zero: '))

if n <= 0:
    print(f'O número {n} não é maior que zero.')
elif (n % 2 == 0) and (n % 3 != 0):
    print(f'O número {n} é divisível por 2.')
elif (n % 2 != 0) and (n % 3 == 0):
    print(f'O número {n} é divisível por 3.')
elif (n % 2 == 0) and (n % 3 == 0):
    print(f'O número {n} é divisível por 2 e por 3.')
else:
    print(f'O número {n} não é divisível por 2 nem por 3.')

# END