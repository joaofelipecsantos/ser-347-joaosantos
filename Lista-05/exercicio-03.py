#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - Joao Felipe
Lista-05
Exercício 03. Tomando como base os operadores disponíveis em Python documentation
- String Methods, apresente as operações para converter os elementos da coluna
string de entrada nos resultados apresentados na coluna string de saída.
"""

# 1
entrada = 'Gilberto'
print(f'++{entrada}++')  # saida = '++Gilberto++'

# 2
entrada = 'sensoriamento remoto'
print(entrada.capitalize())  # saida = 'Sensoriamento remoto'

# 3
entrada = 'sensoriamento remoto'
print(entrada.title())  # saida = 'Sensoriamento Remoto'

# 4
entrada = 'GilberTo'
print(entrada.lower())  # saida = 'gilberto'

# 5
entrada = 'Gilberto'
print(entrada + '**')  # saida = 'Gilberto**'

# 6
entrada = 'Gilberto'
print('**' + entrada)  # saida = '**Gilberto'

# 7
entrada = ' Gilberto'
print(entrada.strip())  # saida = 'Gilberto'

# 8
entrada = 'ser347@dpi.inpe.br'
print("('%s', '@', '%s')" %(entrada.split('@')[0], entrada.split('@')[1]))  # saida = ('ser347', '@', 'dpi.inpe.br')

# 9
entrada = 'CBERS_4_PAN5M_20180308'
print(entrada.split('_'))  # saida = ['CBERS', '4', 'PAN5M', '20180308']

# 10
entrada = 'Gilberto@@@'
print(entrada.replace('@', ''))  # saida = 'Gilberto'

# 11
entrada = '@@Gilberto@@@'
print(entrada.replace('@', ''))  # saida = 'Gilberto'

# END -----------------------