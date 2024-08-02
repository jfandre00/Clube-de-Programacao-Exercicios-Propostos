lista_interna = []

while l < 3:
    for i in range(0,3):
        lista_interna.append(listaTotal[i][l])
    l += 1
listaTotal.append(lista_interna)
