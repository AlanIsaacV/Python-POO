import random
import os

pasos = 1

def busqueda_bin(lista, objetivo):
    global pasos
    pasos = pasos + 1
    medio = len(lista) // 2
    found = False

    # print(f'Buscar en: \n{lista}')
    # print(f'El indice medio es:   {medio}')
    # print(f'El valor que esta en medio es:   {lista[medio]}')
    # print(f'El valor buscado es:   {objetivo}')
    # input('Presiona para continuar...')
    os.system('clear')

    if lista[medio] == objetivo:
        found = True
        return found
    elif lista[medio] != objetivo and medio == 0:
        return found
    elif lista[medio] > objetivo:
        busqueda_bin(lista[:medio], objetivo)
    elif lista[medio] < objetivo:
        busqueda_bin(lista[medio:], objetivo)

if __name__ == '__main__':
    tamano_lista = int(input('Elige el tamaño de la lista:   '))
    objetivo = int(input('Numero a buscar:   '))
    
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    lista.sort()

    if busqueda_bin(lista, objetivo):
        print('Numero encontrado')
    else:
        print(f'No se encontro el numero {objetivo} en la lista')
    
    print(f'Se ejecutaron  {pasos} pasos')