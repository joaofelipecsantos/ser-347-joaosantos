#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - Joao Felipe
Lista-05
Exercício 04. Faça um programa que verifique se uma string é um palíndromo.
Nesse caso, acentos e símbolos devem ser desconsiderados, e não há diferença
entre maiúsculas e minúsculas.
"""

## ENTRADA
palavra = input('Digite uma palavra: ')

## FORMATANDO PALAVRA

# Tudo minusculo
palavraF = palavra.lower()

# Converter acentos
acentos = [['á','â','à','ã','ä','é','ê','è','ë','í','î','ì','ï','ó','ô','ò','ô','õ','ö','ú','û','ù','ü','ç'],
           ['a','a','a','a','a','e','e','e','e','i','i','i','i','o','o','o','o','o','o','u','u','u','u','c']]

for acento, letra in zip(acentos[0],acentos[1]):
    palavraF = palavraF.replace(acento, letra)

# Desconsiderar símbolos
validos = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z']
# Encontrar símbolos
count = 0
while count < len(palavraF):
    if palavraF[count] not in validos:
        palavraF = palavraF.replace(palavraF[count], '*')
    count += 1
# Remover símbolos
palavraF = palavraF.replace('*', '')

## Palavra invertida
inverso = ''
count = len(palavraF) - 1
while count >= 0:
    inverso += palavraF[count]
    count -= 1

## Conferir se é palíndroma
if inverso == palavraF:
    print('É uma palavra palíndroma.')
else:
    print('Não é uma palavra palíndroma.')

# END -----------------------