#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - Joao Felipe
Lista-05
Exercício 02. Para criar uma senha na internet, geralmente são aplicados critérios
de força da senha. Neste exercício, uma senha forte possui caracteres maiúsculos
e minúsculos, e tem pelo menos 8 caracteres. Do contrário, é fraca.
Crie um programa que leia uma senha e retorne se ela é forte ou fraca.
"""

senha = input('Digite sua senha: ')

criterio = 0

# Minimo 8 caracteres
if len(senha) > 8:
    criterio +=1
# Pelo menos uma letra maiuscula
for letra in senha:
    if letra.isupper():
        criterio +=1
        break
# Pelo menos uma letra minuscula
for letra in senha:
    if letra.islower():
        criterio +=1
        break

if criterio == 3:
    print('Senha FORTE.')
else:
    print('Senha FRACA.')

# END -----------------------