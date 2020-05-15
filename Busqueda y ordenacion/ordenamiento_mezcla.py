import os
import random


def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        print (lista, '\n')
        print(f'{izquierda}      {derecha} \n\n\n')

        merge_sort(izquierda)
        merge_sort(derecha)

        i = 0
        j = 0
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1


        print(f'{izquierda}      {derecha}\n')
        print(lista)
        input('Presiona para conrinuar...')
        print('\n\n\n')
        return lista
    

if __name__ == '__main__':
    # tamano_lista = int(input('Ingresa el tamaño de la lista:  '))
    # lista = [random.randint(0, 100) for elemento in range(tamano_lista)]

    lista = [9,8,7,6,5,4,3,2,1,0]
    merge_sort(lista)
    # print(merge_sort())
