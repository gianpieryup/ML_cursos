def inscribir_alumnos():
    """Permite inscribir alumnos al curso"""

    print("Inscripcion en el curso de Algoritmos y ProgramaciÃ³n I")
    inscriptos = []
    while True:
        padron = int(input("Ingresa un padrÃ³n (<=0 para terminar): "))
        if padron <= 0:
            break
        if padron in inscriptos:
            print("El padrÃ³n ya estÃ¡ en la lista de inscriptos.")
            continue
        inscriptos.append(padron)
    return inscriptos

inscriptos = inscribir_alumnos()
print("La lista de inscriptos es:", inscriptos)
