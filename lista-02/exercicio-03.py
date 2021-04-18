#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: SER-347 - João Santos

LISTA - 02
EXERCÍCIO 03
"""

# equacoes
# ndwi = (Xgre - Xnir) / (Xgre + Xnir)
# ndvi = (Xnir - Xred) / (Xnir + Xred)
# Xgre: banda 4 MODIS (545nm - 565nm)
# Xnir: banda 2 MODIS (841nm - 876nm)
# Xred: banda 1 MODIS (620nm - 670nm)

# Definicao dos valores das variaveis
Xgre = 15
Xred = 10
Xnir = 50

# calculo dos indices
# NDWI
ndwi = (Xgre - Xnir) / (Xgre + Xnir)
print('O valor do NDWI é: ', ndwi)
# O valor do NDWI é:  -0.5384615384615384

# NDVI
ndvi = (Xnir - Xred) / (Xnir + Xred)
print('O valor do NDVI é: ', ndvi)
# O valor do NDVI é:  0.6666666666666666

# END