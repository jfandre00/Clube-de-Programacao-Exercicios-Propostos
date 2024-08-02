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
print(listaTotal)



listaA = []
listaB = []
listaC = []
listaD = []
listaE = []
listaF = []
listaG = []
listaH = []
listaI = []

listaH0 = []
listaH1 = []
listaH2 = []
listaH3 = []
listaH4 = []
listaH5 = []
listaH6 = []
listaH7 = []
listaH8 = []


listaH0.append(lista0[0])
listaH0.append(lista1[0])
listaH0.append(lista2[0])
listaH0.append(lista3[0])
listaH0.append(lista4[0])
listaH0.append(lista5[0])
listaH0.append(lista6[0])
listaH0.append(lista7[0])
listaH0.append(lista8[0])


for i in range(0,3):
    listaA.append(lista0[i])
    listaB.append(lista0[i+3])
    listaC.append(lista0[i+6])
    listaD.append(lista3[i])
    listaE.append(lista3[i+3])
    listaF.append(lista3[i+6])
    listaG.append(lista6[i])
    listaH.append(lista6[i+3])
    listaI.append(lista6[i+6])

for i in range(0,3):
    listaA.append(lista1[i])
    listaB.append(lista1[i+3])
    listaC.append(lista1[i+6])
    listaD.append(lista4[i])
    listaE.append(lista4[i+3])
    listaF.append(lista4[i+6])
    listaG.append(lista7[i])
    listaH.append(lista7[i+3])
    listaI.append(lista7[i+6])

for i in range(0,3):
    listaA.append(lista2[i])
    listaB.append(lista2[i+3])
    listaC.append(lista2[i+6])
    listaD.append(lista5[i])
    listaE.append(lista5[i+3])
    listaF.append(lista5[i+6])
    listaG.append(lista8[i])
    listaH.append(lista8[i+3])
    listaI.append(lista8[i+6])



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
    print("NAO")