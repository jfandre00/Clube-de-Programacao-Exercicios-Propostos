'''Um número número 3 é de má sorte se contém um 1 seguido por um 3 entre seus dígitos. Por exemplo, o número 341329 é de má sorte, enquanto o número 26771 ou o número 12321 não é.
Dado um inteiro N, seu programa terá que determinar se N é azarado ou não.

A entrada consiste em um número positivo N (0 <= N <= 10¹⁷).

Saída - Imprima a mensagem "N es de Mala Suerte" se N é de má sorte, caso contrário imprima "N NO es de Mala Suerte".
'''

N=input("Digite o número para sabermos se é boa ou má sorte: ")
lista = []
azarado = False

for c in range (len(N)):
    lista.append(N[c])
    if c > 0:
        if int(lista[c-1]) == 1 and int(lista[c]) == 3:
            azarado = True

if azarado == True :
    print(f'{N} es de Mala Suerte')
else:
    print(f'{N} NO es de Mala Suerte')