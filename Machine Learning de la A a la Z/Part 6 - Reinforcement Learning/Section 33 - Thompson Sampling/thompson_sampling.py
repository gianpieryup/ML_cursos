#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:22:04 2019

@author: juangabriel
"""

# Muestreo Thompson

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

# Algoritmo de Muestreo Thompson
import random
N = 10000
d = 10 # Cant de brazos/maquinas
number_of_rewards_1 = [0] * d # array con la cant de 1's
number_of_rewards_0 = [0] * d # array con la cant de 0's
ads_selected = []
total_reward = 0
for n in range(0, N):
    max_random = 0
    ad = 0
    for i in range(0, d): # "betavariate" es en base a los resultados anteriores
        random_beta = random.betavariate(number_of_rewards_1[i]+1, number_of_rewards_0[i]+1) # Mirar el PDF (Basicamente) con los datos arma una distribucion de Bernouli y toma el valor aleatorio de la distribucion / el que es mas probable de ser la punta
        if random_beta > max_random: # Sacamos el "random_beta" de cada maquina y guardamos el mayor 
            max_random = random_beta
            ad = i
    ads_selected.append(ad) # guardamos la eleccion del mayor
    reward = dataset.values[n, ad] # averguamos el valor si fue 1 o 0 (osea si acepto o no)
    if reward == 1: # en base a lo de arriba  actualizamos los vectores
        number_of_rewards_1[ad] = number_of_rewards_1[ad] + 1
    else:
        number_of_rewards_0[ad] = number_of_rewards_0[ad] + 1
    total_reward = total_reward + reward # Guardamos las recompensas totales
    
# Histograma de resultados
plt.hist(ads_selected)
plt.title("Histograma de anuncios")
plt.xlabel("ID del Anuncio")
plt.ylabel("Frecuencia de visualización del anuncio")
plt.show()

# Como es probabilistico cada corrida del codigo me dara un resultado distinto/ Aparte en comparacion con el metodo de UPC es mejor en cuanto a resultados