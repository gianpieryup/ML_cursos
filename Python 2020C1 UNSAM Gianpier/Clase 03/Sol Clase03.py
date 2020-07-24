#Ejercicio 1.
def ordenada(tupla):
    i = 0
    while i < len(tupla)-1:
        if tupla[i] >= tupla[i+1]:
            return False
        i+=1
    return True

tupla = ('algo','nada','poco')
print(ordenada(tupla))

tupla = (1,45,3.45,-1)
print(ordenada(tupla))



#Ejercicio 2
"""NO entendi si se referian a una funcion o dos funciones"""
#a)
def dominoTupla(t1,t2):
    if len(t1) != 2 or len(t2) != 2:
        print("Longitud incorrecta")
        return False
    if type(t1) != tuple and type(t2) != tuple:
        print("Los argumentos no son tuplas")
    if t1[0] in t2 or t1[1] in t2:
        return True
    else:
        print("No son compatibles")
        
t1=(2,3,4)
t2=(4,5)
print(dominoTupla(t1,t2))

#b)
def dominoString(string):
    lista_dominos = string.split(" ")
    domino1 = lista_dominos[0]
    domino2 = lista_dominos[1]
    print("Domino1:",domino1,"\nDomino2:",domino2)
    
    if len(domino1) != 3 or len(domino2) != 3  :
        print("Longitud incorrecta")
        return False
    
    if domino1[0] in domino2 or domino1[2] in domino2:
        return True
    else:
        print("No son compatibles")

string = '3-4 2-5'
print(dominoString(string))



#Ejercicio 3. Campaña electoral
#a
def votePorMi(tupla):
    for p in tupla:
        print("Estimado",p,",vote por mi")
        
tupla_nombres = ('juan','mario','maría')   
votePorMi(tupla_nombres)

#b
def votacion(tupla,posicionOrigen,n):
    if len(tupla) < posicionOrigen + n:
        print("Posicion de Origen + La cantidad n: excede el limite de la tupla")
    else:
        i = posicionOrigen
        while i < posicionOrigen + n :
            print("Estimado",tupla[i],",vote por mi")
            i+=1
        
tupla_nombres = ('juan','mario','maría','juan','mario','maría')
votacion(tupla_nombres,2,3)

#c
def votePorMiC(tupla):
    for p in tupla:
        print("Estimado",p[0],", cuyo sexo es:",p[1],"vote por mi")
        
tupla_tuplas = (('juan','m'),('mario','m'),('maría','f'))  
votePorMiC(tupla_tuplas)


def votacionC(tupla,posicionOrigen,n):
    if len(tupla) < posicionOrigen + n:
        print("Posicion de Origen + La cantidad n: excede el limite de la tupla")
    else:
        i = posicionOrigen
        while i < posicionOrigen + n :
            print("Estimado",tupla[i][0],", cuyo sexo es:",tupla[i][1],"vote por mi")
            i+=1
        
tupla_tuplas = (('juan','m'),('mario','m'),('maría','f'),('juan','m'),('juan','m'))  
votacionC(tupla_tuplas,2,3)



#Ejercicio 4
# a)
def productoEscalar(vec1,vec2):
    i = 0
    res = 0
    while i < len(vec1):
         res = res + vec1[i]*vec2[i]
         i+=1
    #print("<",vec1,",",vec2,">=",res)     
    return res     
#b)
def ortogonales(vec1,vec2):
    return productoEscalar(vec1,vec2) == 0

#c)
def paralelos(vec1,vec2): 
    i = 0
    k = vec1[0]/vec2[0]
    while i < len(vec1):
         if  vec1[0]/vec2[0] != k:
             return False
         i = i +1
    return True

#d)
def norma(vec): 
   return productoEscalar(vec,vec)**0.5

"""Probando funciones"""
vec1 = (1,2,3)
vec2 = (2,4,6)
print(productoEscalar(vec1,vec2))
print(ortogonales(vec1,vec2))
print(paralelos(vec1,vec2))
print(norma(vec1))


#Ejercicio 5
def funlistas(lista,k):
    lista_menores = []
    lista_iguales = []
    lista_mayores = []
    lista_multiplos = []
    
    for e in lista:
        if e < k:
            lista_menores.append(e)
        if e == k:
            lista_iguales.append(e)
        if e > k:
            lista_mayores.append(e)
        if e%k == 0:    
            lista_multiplos.append(e)
    return {'menores':lista_menores,
            'iguales':lista_iguales,
            'mayores':lista_mayores,
            'multiplos':lista_multiplos}


lista = [1,6,2,9,10,50,60,22]
k = 2
print(funlistas(lista,k))



#Ejercicio 6.
def renombrar(listaTuplas):
    res = []
    for e in listaTuplas:
        res.append( e[1] +' '+ e[2] + ' '+ e[0] )
    return res
   
listaTuplas = [('Bond','James','J.'),('Yupan','Gian','P.')]
print(renombrar(listaTuplas)) 



#Ejercicio 7.
def invertir(lista):
    i = len(lista) - 1
    res = []
    while i > -1 : 
        res.append(lista[i])
        i = i-1
    return res    

lista = ['Di', 'buen', 'día', 'a', 'papa']
print(invertir(lista))

lista[::-1]



#Ejercicio 8
def empaquetar(lista):
    res = []
    i = 0
    contador = 1
    while i < len(lista)-1:
        if lista[i] == lista[i+1]:
            contador += 1
        else:
            res.append((lista[i],contador))
            contador = 1
        i = i + 1
    if lista[i-1] == lista[i]:
        res.append((lista[i],contador))
        
    return res     

lista = [1, 1, 1, 3, 5, 1, 1, 3, 3]
print(empaquetar(lista))



#Ejercicio 9
"""Simpons usted es diabolico"""
#a)
def esMatriz(matriz):
    cantColumnas = len(matriz[0])
    for fila in matriz:
        if len(fila) != cantColumnas:
            return False
    return True   

#Supongo que tienen la misma dimension
def sumarVectores(vec1,vec2):
    i = 0
    res = ()
    while i < len(vec1):
        res+= (vec1[i]+vec2[i],) 
        i+=1
    return res

vec1 = (1,2,3)
vec2 = (1,1,1)

print(sumarVectores(vec1,vec2))

# Voy a asumir que son de la misma dimesion, en un futuro agregare las expeciones
def sumaMatrices(mat1,mat2):
    if esMatriz(mat1) and esMatriz(mat2):
        i = 0
        res = []
        while i < len(vec1):
            res.append(sumarVectores(mat1[i],mat2[i]))
            i+=1
        return tuple(res)
        
    else:
        print("Uno de los argumentos no es una matriz")
    
Matriz1 = ((1,2,3),(4,5,6),(7,8,9))
Matriz2 = ((1,1,1),(2,2,2),(3,3,3))
print(sumaMatrices(Matriz1,Matriz2))

#b)
#Usando la funcion productoEscalar creada ene el ejercicio 4
def columna(matriz,c):
    col =()
    for e in matriz:
        print(e[c])
        col+= (e[c],)
    return col

print(columna(Matriz1,2))


#Supongo las dimensiones de la matriz cumplen los criterios de multiplicacion
def productoMatrizes(mat1,mat2):
    i = 0
    j = 0
    fila =()
    res=[]
    while i < len(mat1):
        while j < len(mat2):
            """Usando la del Ejercicio 4"""
            pE = productoEscalar(mat1[i],columna(mat2,j))
            fila += (pE,)
            j+=1
        res.append(fila)
        fila=()
        j=0
        i+=1
    return  tuple(res)

print(productoMatrizes(Matriz1,Matriz2))

#c)

def sumaMultiple(vec1,vec2,k):
    """return vec1 + vec2*k"""
    i = 0
    res = ()
    while i < len(vec1):
        r = vec1[i] + vec2[i]*k
        res+= (r,) 
        i+=1
    return res

vec1 = (1,2,3)
vec2 = (1,1,1)

print(sumaMultiple(vec1,vec2,-2))


def operacionElemental(Matriz,i,j,k):
    """return i + j*k"""
    res = []
    filai = sumaMultiple(Matriz[i],Matriz[j],k)
    res += Matriz[:i] + (filai,) + Matriz[i+1:]
    return res

Matriz = ((1,1,1),(2,2,2),(3,3,3))
print(operacionElemental(Matriz,1,2,-2))#Probar 


def cambiarFilas(Matriz,i,j):
    """Intercambiamos las filas i por j"""
    res = []
    if i < j:
     #   print(Matriz[:i], (Matriz[j],), Matriz[i+1:j] , (Matriz[i],) , Matriz[j+1:])
        res+= Matriz[:i] + (Matriz[j],) + Matriz[i+1:j] + (Matriz[i],) + Matriz[j+1:] 
    else:
        res+= Matriz[:j] + (Matriz[i],) + Matriz[j+1:i] + (Matriz[j],) + Matriz[i+1:] 
    return tuple(res)

Matriz2 = ((1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5))
print(cambiarFilas(Matriz2,0,2))

def columna(matriz,c):
    col =()
    for e in matriz:
        col+= (e[c],)
    return col

print(columna(Matriz2,2))

def todosCeros(vector):
    for e in vector:
        if e!= 0:
            return False
    return True


vector = (0,0,0,0,1,0)
print(todosCeros(vector))

def elPrimerNoCero(vector):
    for i,e in enumerate(vector):
        if e != 0:
            return i
    return -1
vector = (0,0,1,0,1,0)
print(elPrimerNoCero(vector))


def triangulizar(Matriz):
    res = Matriz
    i=0
    j=1
    while i < len(Matriz[0]): 
        col = columna(res,i)[i:] #Columna desde la diagonal hacia abajo
        print(col)
        if not todosCeros(col):
            #Si hay al menos un numero distinto de cero debajo ó desde la diagonal
            if res[i][i] == 0:# El elemento de la diagonal es = 0
                pNC = elPrimerNoCero(col) + i
                res = cambiarFilas(res,i,pNC)
            #Tengo lo nesesario para arreglar la columna
            while j < len(col):
                if col[j]!=0:               
                   k = col[j]/col[0]
                   print("valor k:",k)
                   res = operacionElemental(res,j+i,i,-k)
                   res = tuple(res)
                j = j + 1
        print(res)        
        i = i+1
        j = 1
    return res    
            
Matriz=((1,2,3),(0,1,1),(2,3,4))
print(triangulizar(Matriz))

#d) (**)
def independenciaLineal(matriz):
    res = triangulizar(matriz)
    return not todosCeros(res[-1])

print("Son l.i. :",independenciaLineal(Matriz))

Matriz2 = ((1,2,3),(0,1,1),(1,2,3))
print("Son l.i. :",independenciaLineal(Matriz2))



#Ejercicio 10
def cortana(texto,longitud):
    texto_cortado = texto.split(" ")
    res = []
    i = 1
    palabra = texto_cortado[0]
    while i < len(texto_cortado):
        if len(palabra) + len(texto_cortado[i]) + 1 > longitud:
            res.append(palabra)
            palabra = texto_cortado[i]
        else:
            palabra = palabra + " " + texto_cortado[i]
        i = i + 1
    res.append(palabra)    
    return res


texto = "A juancito le duele la muela"
longitud = 11
print(cortana(texto,longitud))



#Ejercicio 11
"""Por que nos hacen crear la rueda de nuevo :v :'v  """
#a)
def duplicar(n):
    return n*2

def mapear(f,lista):
    res = []
    for e in lista:
        res.append(f(e))
    return res 
    
lista = [1,2,3]        
print(mapear(duplicar,lista))

#b)
def par(n):
    return n%2==0

def filtrar(f,lista):
    res = []
    for e in lista:
        if f(e):
            res.append(e)
    return res 
    
lista = [1,2,3]        
print(filtrar(par,lista))

#c)
""" No lo se, tu dime ...  XD
    Creo que en el ejercicio 3
"""

#Ejercicio 12
def cifrar(texto,d):#Rescatado de la clase anterior
    i = 0
    res = ""
    while i < len(texto):
        if ord(texto[i]) + d > 122 :
           res = res + chr( ord(texto[i]) + d - 26 )
        else:
           res = res + chr( ord(texto[i]) + d )
        i = i+1
    return res

"""  ord('A') = 65
     ord('Z') = 90
     Hay un salto del 90 al 97
     ord('a') = 97      """
def decifrar(texto,d):
    i = 0
    res = ""
    while i < len(texto):
        if ord(texto[i]) - d < 97 and ord(texto[i]) - d >90 :
            res = res + chr( ord(texto[i]) - d + 26 )    
        else:
            res = res + chr( ord(texto[i]) - d )

        i = i+1
    return res


def cesar(cadena):
    if cadena[0] == "H":#Se debe cifrar
       print("Se debe cifrar")
       cadena = cifrar(cadena,2)# El numero puede ser cualquiera
    else :
        print("Se decifro")
        desplazamiento = ord(cadena[0]) - 72 #El ord('H') = 72
        cadena = decifrar(cadena,desplazamiento)
    return cadena

cadena = "Hola Manuel te envio la carne"
palabra_cifrada = cifrar(cadena,5)
print(cesar(cadena))
print(cesar(palabra_cifrada))


#------------------------------------------------------------
#Ejercicio 13
def cantCoincidencia(lista,elemento):
    cant = 0
    for e in lista:
        if e == elemento:
            cant+=1
    return cant

def posPrimeraCoincidencia(lista,elemento):
    pos = -1
    for i,e in enumerate( lista):
        if e == elemento:
            pos = i
            break
    return pos   

def totalCoincidencia(lista,elemento):
    coincidencias = []
    respaw = 0
    pC = posPrimeraCoincidencia(lista,elemento)
    while pC != -1:
        coincidencias.append(pC+respaw)
        lista = lista[pC+1:]
        respaw +=  pC+1
        pC = posPrimeraCoincidencia(lista,elemento)
        
    return coincidencias
   
lista = [6,3,6,9,3,1,0,5]
elemento = 3        
print(cantCoincidencia(lista,elemento))
print(posPrimeraCoincidencia(lista,elemento))
print(totalCoincidencia(lista,elemento))

#Ejercicio 14.
def maximo(lista):
    maximo = lista[0]
    for e in lista:
        if e > maximo:
            maximo = e
    return maximo


def maximoT(lista):
    maximo = lista[0]
    indice = 0
    for i,e in enumerate(lista):
        if e > maximo:
            maximo = e
            indice = i
    return (maximo,indice)
            

lista = [1,5,2,3,5,7]
print(maximo(lista))
print(maximoT(lista))
print("----------------------------")
"""Funciona igual, usa el criterio de ASCI para comparar cual letra es mayor"""
lista = "Soy una Cadena con y"
print(maximo(lista))
print(maximoT(lista))



#Ejercicio 15.
def agenda(lista_tuplas,cadena):
    res = []
    for e in lista_tuplas:
        if cadena in e[0]:
            res.append(e)
    return res

lista_tuplas = [("Jorge Suarex Yames",11234564),("Maria La Del barrio",11789696),("Beto Suarex Yames",11455478)]
cadena = 'Suar'
print(agenda(lista_tuplas,cadena))



#Ejercicio 16
tupla1 = [(32,"Jabon",60), (33,"Cepillo de dientes",40), (35,"Lavadora",15000)]
tupla2 = [(32,5),(33,2),(35,1)]

def facturar(tupla1,tupla2):
    total_general = 0
    print("Cantidad | Descripcion              | p.u |   Precio")
    for e in tupla1:       
        cant = [t for t in tupla2 if t[0] == e[0]][0][1]
        precio = e[2]*cant if cant >= 3 else e[2]*cant*0.9
        total_general+= precio
        print('{0:5}      {1:20}      {2:5}  {3:8f}'.format(cant, e[1], e[2], precio))
    print("                                      total:",total_general)
    
facturar(tupla1,tupla2)


#Ejercicio 17
def busqueda_binaria(lista, x):
     res = []
     izq = 0
     der = len(lista) - 1

     while izq <= der:
         medio = (izq + der) // 2
         print("[DEBUG]", "izq:", izq, "der:", der, "medio:", medio)

         if lista[medio] == x:
             print("Se encontro en la posicion")
             return medio

         if lista[medio] > x:
             der = medio - 1
         else:
             izq = medio + 1
    
     #SI no esta significa que es la 
     if lista[medio] > x:
        print("x esta entre: [",lista[medio-1],",",lista[medio],"]")
        res = lista[:medio] +[x] + lista[medio:]
        return res

lista_ordenada = [1,3,4,5,9,10,15,20,21,28,30]   
print(busqueda_binaria(lista_ordenada,11))