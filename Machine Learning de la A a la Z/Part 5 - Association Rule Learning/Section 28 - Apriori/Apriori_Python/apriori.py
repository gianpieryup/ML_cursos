#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:05:55 2019

@author: juangabriel
"""

#Apriori

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0,20)])
# Lo convertimos a una lista de listas, donde cada entrada es una lista de lo que compro el usuario

    
    
# Entrenar el algoritmo de Apriori
# Estamos usando el 'paquete' que esta en este directorio 'apyori'
from apyori import apriori
rules = apriori(transactions, min_support = 0.003 , min_confidence = 0.2,
                min_lift = 3, min_length = 2)

# Visualización de los resultados
results = list(rules)

print(results[4])