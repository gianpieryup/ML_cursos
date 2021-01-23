#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:41:01 2019

@author: juangabriel
"""

# Upper Confidence Bound (UCB)

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

# Algoritmo de UCB
import math
N = 10000
d = 10
number_of_selections = [0] * d
sums_of_rewards = [0] * d
ads_selected = []
total_reward = 0
for n in range(0, N):
    max_upper_bound = 0
    ad = 0 # anuncio optimo // ESTE ES EL QUE SE ELIJIRA PARA MOSTRAR AL USUARIO
    for i in range(0, d):
        if(number_of_selections[i]>0): # para no dividir por cero
            average_reward = sums_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(3/2*math.log(n+1)/number_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
            
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1 # Esto al principio del algoritmo sera cero
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward
    

# Y cual es el resultado?    
# Lo puedes ver graficamente con el histograma de abajo
# Me representa todas las veces en la que se presento cada anuncio
    
# Histograma de resultados
plt.hist(ads_selected)
plt.title("Histograma de anuncios")
plt.xlabel("ID del Anuncio")
plt.ylabel("Frecuencia de visualización del anuncio")
plt.show()