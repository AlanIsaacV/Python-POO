import os, random
pasos = 0
def burbuja(lista):
    global pasos
    n = len(lista)
    # os.system('clear')
    # print(lista)
    # input('Presiones una tecla para continuar ...')
    for j in range(n - 2):
        for i in range(n - j - 1 ):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[ i+1 ], lista[i]
            pasos += 1
            # os.system('clear')
            # print(lista)
            # input('Presione una tecla para continuar ...')
    return lista

if __name__ == '__main__':
    tamano_lista = int(input('Ingrese el tamaño de la lista:   '))
    lista = [random.randint(0, 100) for elemento in range(tamano_lista)]
    print(lista)
    print(burbuja(lista))
    print(f'La lista se ordeno en  {pasos} pasos')