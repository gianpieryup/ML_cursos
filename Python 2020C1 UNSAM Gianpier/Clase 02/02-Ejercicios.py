#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:33:38 2020

@author: rgrimson
"""
#%%
import  itertools

print("Las parejas que se pueden formar son:")
for c in itertools.combinations(['Alicia','Bruno','Carlos', 'Diana'],2):
    print("- %s y %s" %(c[0], c[1]))
    
#%%

for c in itertools.permutations('ABCDE',5):
    print(c)

#%%
#Busqueda secuencial
    
x = 25
epsilon = 0.01
paso = epsilon**2
sol = 0.0
totPasos = 0
while abs(sol**2 -x) >= epsilon and sol<x: #Salgo cuando hallo la solucion con poco error o cuando me paso
    sol += paso
    totPasos += 1
    
    
if abs(sol**2 -x) < epsilon: #si encontre la solucion
    print("La raiz de  %f es %f"%(x,sol))
    print("La solucion fue encontrada en %d pasos"%totPasos)
else:
    print("Luego de %d pasos no encontre la solucion"%totPasos)
    
#%%    
#Busqueda por biseccion

x = 25
epsilon = 0.0001
totPasos = 0

cota_inf=0
cota_sup=max(x,1.0)
sol = (cota_inf+cota_sup)/2

while abs(sol**2 -x) >= epsilon: #Salgo cuando hallo la solucion con poco error
    print("busco en [%f, %f], valor medio: %f"%(cota_inf,cota_sup,sol))
    totPasos += 1
    if sol**2 < x:
        cota_inf = sol
    else:
        cota_sup = sol
    sol = (cota_inf + cota_sup) / 2
    
print("busco en [%f, %f], valor medio: %f"%(cota_inf,cota_sup,sol))    
print("La raiz de  %f es %f"%(x,sol))
print("La solucion fue encontrada en %d pasos"%totPasos)

#%%

P=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]

