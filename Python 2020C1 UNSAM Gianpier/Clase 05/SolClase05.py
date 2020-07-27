import log
# Pedimos el nombre del archivo
nombre = input("Nombre: ")

""" Cuando todas empiezan con letras, no hay problema
    Si tienen disntinto formato usar,este
    open(filename, encoding="utf8")
"""

with open(nombre, encoding="utf8") as archivo:
    for i, linea in enumerate(archivo):
        linea = linea.rstrip("\n")
        print("{}: {}".format(i, linea))

if error:
    log.guardar(archivo_log, "ERROR: " + error)


log.cerrar(archivo_log)


