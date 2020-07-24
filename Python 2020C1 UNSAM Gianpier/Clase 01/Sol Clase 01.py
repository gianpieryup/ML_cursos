# EJERCICIO 7
def vocaloid(cadena):
    i = 0
    res = ""
    vocales = ['a','e','i','o','u']
    while i < len(cadena):
        if  cadena[i] in vocales:
            res = res + '-'
        else :
            res = res + cadena[i]
        i = i+1
    return res
    
print(vocaloid("manuelito el sapito"))

# EJERCICIO 9
def invertir(cadena):
    i = len(cadena)-1
    res = ""
    while i >= 0:
        res = res + cadena[i]
        i = i-1
    return res
    
print(invertir("papurra"))


# EJERCICIO 10
# Prueba de ASCI
print(ord('a'))#97
print(ord('b'))#98
print(ord('x'))#120
print(ord('X'))#88
print(ord('z'))#122

def cifrar(texto,d):
    i = 0
    res = ""
    while i < len(texto):
        if ord(texto[i]) + d > 122 :
           res = res + chr( ord(texto[i]) + d - 26 )
        else:
           res = res + chr( ord(texto[i]) + d )
        i = i+1
    return res

print(cifrar("AbcDefuvwxyz",4))    