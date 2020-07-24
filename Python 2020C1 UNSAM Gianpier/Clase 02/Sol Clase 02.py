#Ejercicio 1.
lenguajes = ["Pyhton", "C++", "C", "Pascal"]
for num , l in enumerate ( lenguajes ):
    print (num ,":", l )

#Ejercicio 2.
def comprimir(S):
    res = ""
    for indice, letra in enumerate(S):
        if letra != " ":
            if S[indice - 1] == " ":
                res += letra.upper()
            else:
                res += letra
    return res
    
S = "una frase muy larga, de verdad muy larga"
S_com = comprimir(S)    
print("S comprimida : ",S_com)

def descomprimir(S):
    res = ""
    for indice, letra in enumerate(S):
        if letra == letra.upper():#Si la letra es mayuscula
            res = res + " " + letra.lower()
        else:# Si es minuscula
            res += letra
    return res

S_des = descomprimir(S_com)
print("S descomprimida : ",S_des)


#Ejercicio 3.
s1 = "Paseo el perro por la vereda" 
s2 = "perro"
print("La primera ubicacion coincide : ",s1.find(s2))


#Ejercicio 4.
def tabla(num):
    for n in range(0,10):
        print( str(num)+ " *  "+ str(n) + " = " +str(num*n) + "\t" )
tabla(7)


#Ejercicio 5.
entrada = ["ensalada", "camarones", "guacamole", "lengua","humus"]
plato_principal = ["ppa","ppb","ppc","ppd","ppe"]
postre = ["pa","pb","pc","pd","pe"]

#5.1
for e in entrada:
    for pp in plato_principal:
        for pos in postre:
            print("entrada:",e,"| Plato Principal:",pp,"| Postre:",pos)


#5.2
""" Como me tienen que decir cuales comidas son veganas, entonces puedo filtrar las listas
Antes de hacer los ciclos 'for' , de lo contrario estaria recorriendo elementos que no utilizare
"""            
entrada_veg = ["ensalada","humus"]
plato_principal_veg = ["ppa","ppe"]
postre_veg = ["pa","pc"]    
for e in entrada_veg:
    for pp in plato_principal_veg:
        for pos in postre_veg:
            print("entrada:",e,"| Plato Principal:",pp,"| Postre:",pos)            

#5.3
"""Como son 5 pues predefino lo que comera, asi no comero dos veces el mismo plato
"""            
for i in range(0,5):
    print("entrada:",entrada[i],"| Plato Principal:",plato_principal[i],"| Postre:",postre[i])

#6 aca se usa intertool para los puntos, easy
import itertools

#6.1
print("Conductor - Copiloto")
for c in itertools.permutations (['Alicia','Bruno ','Carlos ', 'Diana '] ,2):
    print ("- %s y %s" %(c[0] , c [1]) )

#6.2
for c in  itertools.product('ABCDE', 'ABCDE') :
    print(c[0]," y ",c[1])

#6.3
for c in  itertools.permutations('ABCDE', 5) :
   print(c[0]+c[1]+c[2]+c[3]+c[4])    


#7 Coronavirus
def bloques(num,cantidad):
    res = []
    for x in range(cantidad):
        res.append(num)
    return res

def cuarentena(pacientes):
    res = []
    bloque = []
    for i,p in enumerate(pacientes):
        if(p == 0 or i == len(pacientes)-1):#Se corta un bloque de infectados hasta encontrar uno sano(0) o bien es el ultimo bloque
            if(-1 in bloque):#Hay un infectado en el bloque
                res = res + bloques(-1,len(bloque))
            else:
                res = res + bloques(1,len(bloque))
            res.append(0)
            bloque = []
        else :
            bloque.append(p)
    res.pop()#En la ultima iteracion se dejo un 0 extra que hay que borrar
    return res

res = cuarentena([ 1, 1, 1, 0,-1, 1, 1, 1, 0, 1,-1, 1, 1])
res2 =cuarentena([ 1, 1, 1,-1, 1, 1])
print(res)
print(res2)



# EJERCICIO 8
# Se resolvio en la guia1 con while
def vocaloid(cadena):
    res = ""
    vocales = ['a','e','i','o','u']
    for c in cadena:
        if c in vocales:
            res = res + '-'
        else :
            res = res + c
    return res    

print(vocaloid("manuelito el sapito"))  


# EJERCICIO 9 
print("Cuántos pasos tarda en encontrar una raiz de 25? \n49990 pasos")
print("Cuantos pasos tarda en encontrar una raiz de 30? \n54764 pasos ")
print("Cuál es la precision del metodo? \n0.0001")
print("Si quisiera duplicar la precision (es decir, dividir por dos el error maximo que puedo cometer)\nCuantos pasos más me tomaria hallar la raiz de 30? \nMe tomaria 219071 pasos\nEn comparacion al anterior 164,307 pasos extra acambio de tener mayor precicion")


# EJERCICIO 10
print("Cuántos pasos tarda en encontrar una raiz de 25? \n19 pasos")
print("Cuantos pasos tarda en encontrar una raiz de 30? \n19 pasos ")
print("Cuál es la precision del metodo? \n0.0001")
print("Si quisiera duplicar la precision (es decir, dividir por dos el error maximo que puedo cometer)\nCuantos pasos más me tomaria hallar la raiz de 30? \nMe tomaria 19 pasos\nEn comparacion al anterior la misma cantidad, esto ocurre por que el resultado anterior tiene un error menor al 0.0000265 que es (<) 0.00005")


# EJERCICIO 11
# Usar el TAB me hace 4 veces mas productivo por tecla
# SECUENCIAL
def secuencial(elemento,lista):
    totPasos=0
    for i,n in enumerate(lista):
        totPasos += 1
        if(n==elemento):
            print("Pasos:",totPasos,"| Res: Se Encontro")
            return i
    print("Pasos:",totPasos,"| Res: NO se Encontro")    
    return -1

print("Posicion:",secuencial(45,[10,20,30,40,50]) )

def binaria(elemento,lista):
    """
    Busqueda de un elemento en una lista de forma binaria:
        Osea reduciendo a la mitad la cantodad de valores posibles en cada iteracion
    """
    totPasos=0
    cota_inf = 0
    cota_sup = len(lista)-1
    pos = ( cota_inf + cota_sup )//2

    while cota_sup - cota_inf >1 : 
        totPasos += 1
        #print ("busco entre [ {0}, {1}], valor medio : {2}".format(lista[cota_inf] ,lista[cota_sup] ,lista[pos]))
        if lista[pos] < elemento:
            cota_inf = pos
        else :
            if lista[pos] == elemento:            
                break
            else:
                cota_sup = pos
        pos = ( cota_inf + cota_sup )//2
    
    #Acepciones
    if  lista[pos+1] == elemento:
            pos = pos +1
    else: # No es el siguiente       
        if  lista[pos] != elemento:
            print("Pasos:",totPasos,"| Res: NO se Encontro")  
            return -1
  
    print("Pasos:",totPasos,"| Res: Se Encontro")   
    return pos
          
lista = [10,20,30,40,50,60,70]
elem = 50
print("Posicion:",binaria(elem,lista))


#Ejercicio 13
P=[2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37 , 41 , 43 , 47 , 53 , 59 , 61 , 67 , 71 , 73 , 79 , 83 , 89 , 97 ,
101 , 103 , 107 , 109 , 113 , 127 , 131 , 137 , 139 , 149 , 151 , 157 , 163 , 167 , 173 , 179 , 181 , 191 ,
193 , 197 , 199 , 211 , 223 , 227 , 229 , 233 , 239 , 241 , 251 , 257 , 263 , 269 , 271 ]

#Pruebas
secuencial(128,P)
binaria(128,P)
print("------------")
secuencial(37,P)
binaria(37,P)
print("------------")
secuencial(176,P)
binaria(176,P)
print("------------")
secuencial(167,P)
binaria(167,P)
print("------------")
secuencial(286,P)
binaria(286,P)
print("------------")
secuencial(1,P)
binaria(1,P)

   
#Ejercicio 14
# 0 = abajo y 1 = arriba
# El juego toma la carta arriba(1) y cambia la drecha
def paso(lista):
    if 1 not in lista[:-1] :
        print("NO hay mas jugadas disponibles")
        return -1  
    res = []
    for i,c in enumerate(lista):
        if c == 1:# esta la volteo
            #REcordar el [:j]  la posicion j no la considera
            res = lista[0:i] + [0]
            if lista[i+1] == 1:
                res = res +[0]+lista[i+2:]
            else:
                res = res +[1]+lista[i+2:]   
            break 
    
    return res 
       
C = [0,0,0,1,0,1,1]           
print(paso(C))

def jugar(lista):
    res = lista
    while res!=-1:
        print(res)
        res = paso(res)

jugar(C)


#Ejercicio 14*
"""Por su pollo
Veremos que no se pueda jugar infinitamente
Cada jugada puede ser de la siguiente manera:
[1,1] => [0,0]
[1,0] => [0,1] 
Entonces la cantidad de ceros nunca disminuye solo puede aumentar

Por contradiccion para jugar infinitamente deben haber solo jugadas finitas
del tipo [1,1] => [0,0], ya que si son infinitas la cantidad de 1's caeria a 0 y ya no se podria jugar

Digamos que sea cierto, entonces habra un punto donde ya no exista [1,1] en toda la lista
por lo cual nos quedaria lo siguiente
[0..0,1,0..0,1,0..0]
Que a exepcion de los bordes si existe un 1 en la lista, nesesariamente atras y adelante hay ceros
[0,1,0]
Entonces si puedo jugar infinitamente tendria que ser nesesariamente
[0,0,1]
Luego como la cantidad de elementos es finita, llegara un punto en el que
[0..0,0,1,1] me queden dos 1's pegados a la derecha, pero esto es imposible
debido a la supocicion anterior
Por tanto el juego tiene fin 

"""

import random
carta_cara_arriba =( random . random () < 0.5)