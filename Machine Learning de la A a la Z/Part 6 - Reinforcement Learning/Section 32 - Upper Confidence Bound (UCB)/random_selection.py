#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:21:01 2019

@author: juangabriel
"""

# Selección Aleatoria


# Importar las librarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementrar una Selección Aleatoria
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward

""" Lo que hacemos es elegir en cada ronda un anuncio del [1 al 10]
    para mostrarle al usuario
    Si comparamos las siguientes variables
    ads_selected  y dataset
    notaremos en "ads_selected" que anuncio se eligio mostrar al usuario(i)
    Y con "dataset" sabremos si lo eligio o no
    
    Ademas en "total_reward" tenemos todas las veces en la que el usuario 
    acepto ver el anuncio que se escogio.

"""

# Visualizar los resultados - Histograma
plt.hist(ads_selected)
plt.title('Histograma de selección de anuncios')
plt.xlabel('Anuncio')
plt.ylabel('Número de veces que ha sido visualizado')
plt.show()

# Esto ultimo nos dice que los 10 anuncios se an mostrado con una frecuencia 
# muy parecida