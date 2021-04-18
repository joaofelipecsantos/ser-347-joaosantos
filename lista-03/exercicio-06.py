#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 06. Faça um programa que pergunte ao usuário o seu conceito final em
uma disciplina hipotética. Dependendo do conceito digitado, diga o que ele significa.
"""

# Definindo os conceitos
conceito_list = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D']
definicao = ['Excepcional', 'Excelente', 'Excelente', 'Bom', 'Bom', 'Bom',
             'Regular', 'Regular', 'Regular', 'Reprovação']

x = input('Digite o seu conceito final em uma disciplina para saber a definição: ')

if x not in conceito_list:
    print(f"O conceito '{x}' não existe.\nOpções: 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D'")
else:
    count = 0
    while count < 10:
        if x == conceito_list[count]:
            print(f"O conceito '{x}' significa '" +definicao[count] +"'.")
            break
        else:
            count+=1

# END