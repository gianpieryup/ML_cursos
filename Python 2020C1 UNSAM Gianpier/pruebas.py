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

    