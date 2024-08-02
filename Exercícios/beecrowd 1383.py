lista0 = [1, 3, 2, 5, 7, 9, 4, 6, 8]
lista1 = [4, 9, 8, 2, 6, 1, 3, 7, 5]
lista2 = [7, 5, 6, 3, 8, 4, 2, 1, 9]
lista3 = [6, 4, 3, 1, 5, 8, 7, 9, 2]
lista4 = [5, 2, 1, 7, 9, 3, 8, 4, 6]
lista5 = [9, 8, 7, 4, 2, 6, 5, 3, 1]
lista6 = [2, 1, 4, 9, 3, 5, 6, 8, 7]
lista7 = [3, 6, 5, 8, 1, 7, 9, 2, 4]
lista8 = [8, 7, 9, 6, 4, 2, 1, 5, 3]

listaTotal = []

listaTotal.append(lista0)
listaTotal.append(lista1)
listaTotal.append(lista2)
listaTotal.append(lista3)
listaTotal.append(lista4)
listaTotal.append(lista5)
listaTotal.append(lista6)
listaTotal.append(lista7)
listaTotal.append(lista8)

'''
for n in range(0,9):
    lista = list(map(int, input().split()))
    listaTotal.append(lista)

'''
l = 0
lista_vertical = []

while l < 9:
    for i in range(0,9):
        lista_vertical.append(listaTotal[i][l])
            
    listaTotal.append(lista_vertical)

    lista_vertical = []
    l += 1

l = 0
lista_interna = []
contador = 0

while contador < 9:
    while l < (3 + contador):
        for i in range(0,3):
            lista_interna.append(listaTotal[i][l])
        l += 1
    listaTotal.append(lista_interna)
    lista_interna = []
    contador += 3
  
l = 0
contador = 0
while contador < 9:
    while l < (3 + contador):
        for i in range(3,6):
            lista_interna.append(listaTotal[i][l])
        l += 1
    listaTotal.append(lista_interna)
    lista_interna = []
    contador += 3

l = 0
contador = 0
while contador < 9:
    while l < (3 + contador):
        for i in range(6,9):
            lista_interna.append(listaTotal[i][l])
        l += 1
    listaTotal.append(lista_interna)
    lista_interna = []
    contador += 3

print(listaTotal)