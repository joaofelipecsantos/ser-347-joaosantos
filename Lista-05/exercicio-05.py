#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - Joao Felipe
Lista-05
Exercício 04. Faça um programa que leia uma frase e verifique se é um palíndromo.
Nesse caso, os espaços, acentos e símbolos devem ser desconsiderados, e não há
diferença entre maiúsculas e minúsculas.
"""

# ENTRADA
frase = input('Digite uma frase: ')

# FORMATANDO frase
# 1 - Sem espaço
fraseF = frase.replace(' ','')

# 2 - Tudo minusculo
fraseF = fraseF.lower()

# 3 - Converter acentos
acentos = [['á','â','à','ã','ä','é','ê','è','ë','í','î','ì','ï','ó','ô','ò','ô','õ','ö','ú','û','ù','ü','ç'],
           ['a','a','a','a','a','e','e','e','e','i','i','i','i','o','o','o','o','o','o','u','u','u','u','c']]

for acento, letra in zip(acentos[0],acentos[1]):
    fraseF = fraseF.replace(acento, letra)

# 4 - Desconsiderar símbolos
validos = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z']
# Encontrar símbolos
count = 0
while count < len(fraseF):
    if fraseF[count] not in validos:
        fraseF = fraseF.replace(fraseF[count], '*')
    count += 1
# Remover símbolos
fraseF = fraseF.replace('*', '')

# frase invertida
inverso = ''
count = len(fraseF) - 1
while count >= 0:
    inverso += fraseF[count]
    count -= 1

if inverso == fraseF:
    print('É uma frase palíndroma.')
else:
    print('Não é uma frase palíndroma.')

# END -----------------------