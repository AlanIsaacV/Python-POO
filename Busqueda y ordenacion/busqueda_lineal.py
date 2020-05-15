import random

def busqueda_lineal(lista, objetivo):
    found = -1
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            found = indice
            break
    return found

def main():
    tamano_lista = int(input('Ingresa el tamaño de la lista:   '))
    objetivo = int(input('Numero a buscar:   '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print (lista)
    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El elemento  {objetivo} {f"esta en la posicion {encontrado}" if (encontrado >= 0) else "no esta en la lista"} ')


if __name__ == '__main__':
    main()