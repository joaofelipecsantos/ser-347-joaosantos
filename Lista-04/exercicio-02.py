#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - João Felipe
Lista-04
Exercício 02. Escrever um programa em Python que simule uma calculadora com as
funções básicas (+, −, ÷, ×). O programa deve pedir ao usuário para entrar com
os operandos (números reais) e o tipo de operação, e a seguir escrever o resultado.
Assim como uma calculadora, que ao final de uma operação pode ser utilizada
novamente, você deve simular este comportamento perguntando ao usuário se ele
quer realizar uma nova operação.
"""

# Definição das operações possíveis
operacao_list = ['+', '-', '/', '*']

# Informação para o usuário
print('Digite os operandos (números reais) e o tipo de operação (+, −, /, ∗).')

# Condição inicial
calcular = True

# Primeiro número só entra uma vez
a = float(input('Primeiro número: '))

while calcular == True:
    # Definição de existência da operacao
    existencia = True

    # Entradas
    b = float(input('Segundo número: '))
    operacao = (input('Operação: '))

    # Caso onde a operação não existe
    if operacao not in operacao_list:
        print(f"A operação '{operacao}' não pode ser realizada.\nOpções: '+', '−', '/', '∗'")
        existencia = False  # Não vai mostrar resultado no final
        pergunta = input('Deseja recomeçar? [S]/n: ')
        if (pergunta == '') or (pergunta == 'S') or (pergunta == 's'):
            a = float(input('Primeiro número: '))
        else:
            exit()
    # Caso do divisor ser igual a zero
    elif (operacao == '/') and (b == 0):
        print(f"A operação '{operacao}' não pode ser realizada.\nErro: divisor igual a zero.")
        existencia = False  # Não vai mostrar resultado no final
        pergunta = input('[R]Recomeçar | [E]Editar : ')
        if (pergunta == 'R') or (pergunta == 'r'):
            a = float(input('Primeiro número: '))
        elif (pergunta == 'E') or (pergunta == 'e'):
            print('Digite novamente o segundo número e a operação.')
        else:
            existencia = False

    # Operações
    elif operacao == '+':
        resultado = a + b
    elif operacao == '-':
        resultado = a - b
    elif operacao == '/':
        resultado = a / b
    else:
        resultado = a * b
    
    if existencia == True:
        print(f"{a} {operacao} {b} = ", str(round(resultado, ndigits=1)))
        pergunta = input('[C]Continuar | [R]Recomeçar | [P]Parar : ')
        if (pergunta == 'C') or (pergunta == 'c'):
            a = resultado
        elif (pergunta == 'R') or (pergunta == 'r'):
            a = float(input('Primeiro número: '))
        else:
            calcular = False

# END
