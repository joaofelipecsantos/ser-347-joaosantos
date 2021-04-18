#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SER-347 - Joao Felipe
Lista-05
Exercício 01. Arquivo com nome MOD09A1.A2006001.h08v05.005.2006012234657.hdf
MOD09A1 - Product Short Name
MOD: Terra Satellite
A2006001 - Julian Date of Acquisition (A-YYYYDDD)
h08v05 - Tile Identifier (horizontalXXverticalYY)
005 - Collection Version
2006012234567 - Julian Date of Production (YYYYDDDHHMMSS)
hdf - Data Format (HDF-EOS)
"""

# Formato de saida:
#Satellite...............: Terra
#Product.................: MOD09A1
#Year of Acquisition.....: 2006
#Julian Day..............: 001
#Horizontal Tile.........: 08
#Vertical Tile...........: 05
#Collection..............: 005
#Year of Production......: 2006
#Julian Day of Production: 012
#Production Hour.........: 23
#Production Minute.......: 46
#Production Second.......: 57
#Data Format.............: hdf

def lista_de_resultados(output):
    resultados.append(output)

arquivo = 'MOD09A1.A2006001.h08v05.005.2006012234657.hdf'
arquivo_split = arquivo.split('.')
lista_de_parametros = ['Satellite',
                       'Product',
                       'Year of Acquisition',
                       'Julian Day',
                       'Horizontal Tile',
                       'Vertical Tile',
                       'Collection',
                       'Year of Production',
                       'Julian Day of Production',
                       'Production Hour',
                       'Production Minute',
                       'Production Second',
                       'Data Format']

# Foi dito em aula que o programa é somente para esse produto,
# Então Satellite = Terra (sempre)
resultados = ['Terra']

# Product
prod = arquivo_split[0]
lista_de_resultados(prod)
# Year of Acquisition
acquisitionY = arquivo_split[1][1:5]
lista_de_resultados(acquisitionY)
# Julian Day
acquisitionJD = arquivo_split[1][5:8]
lista_de_resultados(acquisitionJD)
# Horizontal Tile
ht = arquivo_split[2][1:3]
lista_de_resultados(ht)
# Vertical Tile
vt = arquivo_split[2][4:6]
lista_de_resultados(vt)
# Collection
collection = arquivo_split[3]
lista_de_resultados(collection)
# Year of Production
productionY = arquivo_split[4][0:4]
lista_de_resultados(productionY)
# Julian Day of Production
productionJD = arquivo_split[4][4:7]
lista_de_resultados(productionJD)
# Production Hour
productionH = arquivo_split[4][7:9]
lista_de_resultados(productionH)
# Production Minute
productionM = arquivo_split[4][9:11]
lista_de_resultados(productionM)
# Production Second
productionS = arquivo_split[4][11:13]
lista_de_resultados(productionS)
# Data Format
data_format = arquivo_split[-1]
lista_de_resultados(data_format)

# Definindo o numero maximo de caracteres no nome dos parametros
# para completar o resto com pontos
maior_string = 0
for parametro in lista_de_parametros:
    if len(parametro) > maior_string:
        maior_string = len(parametro)

print(f'File {arquivo}\n')
for parametro, resultado in zip(lista_de_parametros, resultados):
    parametro_name = parametro + '.' * (maior_string - len(parametro)) + ':'
    print(parametro_name, resultado)

# END -----------------------