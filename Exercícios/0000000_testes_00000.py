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

l = 0
lista_vertical = []

while l < 9:
    for i in range(0,9):
        lista_vertical.append(listaTotal[i][l])
            
    listaTotal.append(lista_vertical)

    lista_vertical = []
    l += 1

##Automatização a
l = 0
lista_interna = []
contador = 0
cont = 0

while contador < 9:
    while l < (3 + contador):
        for i in range(cont,3 + cont):
            lista_interna.append(listaTotal[i][l])
        l += 1
    listaTotal.append(lista_interna)
    lista_interna = []
    contador += 3

cont = 3   
l = 0
contador = 0
while contador < 9:
    while l < (3 + contador):
        for i in range(cont, 3+cont):
            lista_interna.append(listaTotal[i][l])
        l += 1
    listaTotal.append(lista_interna)
    lista_interna = []
    contador += 3

l = 0
contador = 0
cont = 6
while contador < 9:
    while l < (3 + contador):
        for i in range(cont, 3+cont):
            lista_interna.append(listaTotal[i][l])
        l += 1
    listaTotal.append(lista_interna)
    lista_interna = []
    contador += 3

print(listaTotal)

'''
#Fazer da lista0 até lista8 / da listaA até listaI
if (1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9) in lista0:
    verificacao_1 = True

#Fazer da listaA até listaI
if (1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9) in listaA:
    verificacao_2 = True

#Fazer da listaH0 até listaH8
if (1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9) in listaH0:
    verificacao_3 = True

#Fazer a verificação da soma de todas as listas
if sum(lista0) == 45:
    print("Soma ok")



if (verificacao_1 and verificacao_2 and verificacao_3) == True:
    print("SIM")
else:
    print("NAO")'''