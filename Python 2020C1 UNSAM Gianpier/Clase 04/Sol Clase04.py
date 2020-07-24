#Ejercicio 1.
def tuplas_a_diccionario(lista):
    i=0
    lista_dicc=[]
    clave = lista[0][0]
    diccionario = {}
    while len(lista) !=0:
        print("La lista",lista)
        if lista[i][0] == clave:
           lista_dicc.append(lista[i][1])
           lista = lista[:i] + lista[i+1:]
           print("lista despues del ",lista)
        else:
           i=i+1   
        print("como quedo el i=",i)   
        if i==len(lista):
           i=0
           diccionario[clave]=lista_dicc
           if lista != []:
               clave=lista[0]  
    return diccionario
      
lista = [('Hola','don Pepito'),('Hola', 'don Jose')]                           
print(tuplas_a_diccionario(lista))

#Ejercicio 2.
#a)
def diccontar(frase):
    lista_palabras = frase.split(" ")
    dicc={}
    dicc[lista_palabras[0]] = 0
    for p in lista_palabras:
        if p in dicc :
            dicc[p]+=1
        else :
            dicc[p]=1
    return dicc
        
frase = "Hay grandes libros en el mundo y grandes mundos en los libros"
print(diccontar(frase))
"""FE RATAS : en el PDF 'en':1 incorrecto debe ser 2"""


#b)
def numeral(cantidad):
    res = ''
    for i in range(cantidad):
        res+='#'
    return res

def contadorLetras(cadena):
    dicc={}
    dicc[cadena[0]] = 0
    for p in cadena:
        if p in dicc :
            dicc[p]+=1
        else :
            dicc[p]=1
    
    #print(dicc)
    for k in dicc.keys():
        print(k,numeral(dicc[k])) 

cadena = 'Abracadabra'  
contadorLetras(cadena) 



#Ejercicio 3.
import random   

def simulador():
    i=0
    lista=[]
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    while i < 100:
        lista.append((dado1,dado2))
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        i+=1
    return lista    
  
def cantResultados(lista):      
    dicc={}
    dicc[lista[0][0]+lista[0][1]] = 0
    for p in lista:
        pos = p[0]+p[1]
        if pos in dicc :
            dicc[pos]+=1
        else :
            dicc[pos]=1
    for k in range(2,13):
        if(k in dicc):
            print("{0:2} {1}".format(k,numeral(dicc[k]) ) )
        else:
            print(k,'')
                
lista = simulador()
cantResultados(lista)




#Ejercicio 4.
"""
Tube un percanse lo busque en stack Overflow
Soy consciente de que no puede agregar / eliminar elementos en un diccionario mientras lo itera
"""

def agenda():
    nombre = input("Ingrese un nombre:")
    dicc= {'eduardo':11203987,'ricardo':11239564,'maria':11748596}
    while nombre != '*':
        if nombre[0]=='-':#borrar
            nombre=nombre[1:]           
            for e in list(dicc):
                if nombre in e:
                    print("DELETE",e,dicc[e])
                    dicc.pop(e)
            print("termine de quitar")       
        else:
            if nombre[0]=='?':#cambiar el valor
                nombre=nombre[1:]
                texto_asociado = input("Texto Asociado:")
                for e in dicc:
                    if nombre in e:
                        print("UPDATE",e,texto_asociado)
                        dicc[e]=texto_asociado     
            else:       
                if nombre[0]=='+':
                    nombre=nombre[1:]
                
                res = {}
                for n in dicc:
                    if nombre in n:
                        res[n]=dicc[n]
            
                if len(res)>0:
                    print(res)
                else:#NO se encontro ninguna busqueda parcial con este nombre
                    print('No se encontro ninguna coincidencia\nPor favor ingrese un texto asociado')
                    texto_asociado = input("Texto Asociado:")
                    dicc[nombre]=texto_asociado
        
        nombre = input("Ingrese un nombre:")
        
agenda()


#Conjuntos


#Ejercicio 5
#a)
#No hay nesesidad de usar el else y otro return 
def Abs(i):
    """Devuelve el valor absoluto de i
    """
    if i <0:
        i*=-1
    return i  


#b)
#No hay nesecidad de tranformar el diccionario en una lista de duplas
diccionario = {'uno':'abc@gmail.com','dos':'cdegmail.com'}
def emails(diccionario):
    """Imprime las (clave - valor) de un diccionario, con cierto formato
    """
    for e in diccionario:
        print(f"El e-mail de {e} es {diccionario[e]}")
emails(diccionario)


#c)
#Como devuelvo una lista, puedo hacer uso de listas comprimidas
def emails2(diccionario):
    """Devuelve el diccionario sin los elementos cuyo valor, no posea el caracter '@'
    """
    return dict([(e,diccionario[e]) for e in diccionario if '@' in  diccionario[e]])

print(emails2(diccionario))


#d)
nombres = ['Av larco','Eduardo Nordelta','Geminis']
direcciones = {'Av larco':12,'Nueva Pompeya':14,'Jiron juventud':1646}
   
#Se puede mejorar los nombres de las variables y se recorre de manera ineficiente la lista de nombres
def emails3(nombres, direcciones={}):
    """Toma una lista de nombres y revisa si existen en el diccionario direcciones
       Para los nombres que no esten en las direcciones, se creara una direccion nueva con esta clave
    """
    for nombre in nombres:
        if (nombre not in direcciones):
            n_y_a = nombre.lower().split(' ')
            direcciones[nombre] = n_y_a[0] + '.' + n_y_a[-1] + '@unsam.edu.ar'
    return direcciones

#Si solo pasamos un apodo: El valor sera apodo.apodo@unsam.edu.ar
print(emails3(nombres, direcciones))

#Si no pasamos el diccionario, tomara el valor {} que fue definido en la funcion en caso no se pasara
print(emails3(nombres))
