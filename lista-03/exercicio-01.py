#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 01. Faça um programa em Python que leia três números reais e escreva
o valor do maior e do menor deles.
"""

print('Digite três números.')

# Números reais
a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))


if a > b and a > c:
    if b > c:
        print(f'{a} é o maior número e {c} é o menor.')
    else:
        print(f'{a} é o maior número e {b} é o menor.')
elif b > a and b > c:
    if a > c:
        print(f'{b} é o maior número e {c} é o menor.')
    else:
        print(f'{b} é o maior número e {a} é o menor.')
else:
    if a > b:
        print(f'{c} é o maior número e {b} é o menor.')
    else:
        print(f'{c} é o maior número e {a} é o menor.')

# END