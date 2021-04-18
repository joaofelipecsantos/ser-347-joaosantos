#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
lista-03
Exercício 07. Escreva um programa em Python que simule uma calculadora com as
4 funções básicas (+, −, /, ∗). O programa deve pedir ao usuário para entrar
com os operandos (números reais) e o tipo de operação, e a seguir escrever o resultado.
"""

# Definição das operações possíveis
operacao_list = ['+', '-', '/', '*']
# Definição de existência da operacao
existencia = True

# Informação para o usuário
print('Digite os operandos (números reais) e o tipo de operação (+, −, /, ∗).')

# Inputs
a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
operacao = (input('Operação: '))

if operacao not in operacao_list:
    print(f"A operação '{operacao}' não pode ser realizada.\nOpções: '+', '−', '/', '∗'")
    existencia = False  # Não vai mostrar resultado no final
elif operacao == '+':
    resultado = a + b
elif operacao == '-':
    resultado = a - b
elif operacao == '/':
    resultado = a / b
else:
    resultado = a * b

if existencia == True:
    print(f"O resultado da operação ({a} {operacao} {b}) é", str(round(resultado, ndigits=1)) +'.')

# END