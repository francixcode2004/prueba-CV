def calcular_eficiencia(lista):
    eficiencia=0
    for i in  range(len(lista)):
        eficiencia+=lista[i]*(i+1)
    return eficiencia
def crear_arreglo(entrada):
    try:
        numeros = [int(num) for num in entrada.split()]
    except ValueError:
        print("Ingresa solo números separados por espacios por favor")
        return []
    indice_arreglo = numeros.index(max(numeros)) if max(numeros) in numeros else -1
    if indice_arreglo != -1:
        nuevo_arreglo = numeros[indice_arreglo:indice_arreglo+max(numeros)]
        arreglo_ordenado =sorted(nuevo_arreglo)
        return arreglo_ordenado
    else:
        print("No se encontro el mayor de la lista :(")
        return []
entrada_usuario =input("Ingrese los números: ")
lista_numeros = crear_arreglo(entrada_usuario)
print("Nuevo arreglo:", lista_numeros)
resultado_eficiencia = calcular_eficiencia(lista_numeros)
print("La eficiencia es:", resultado_eficiencia)