'''Beatriz retira as cinco primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequência, da esquerda para a direita, na mesa, com as faces voltadas para baixo. 
Faça um programa que, dada uma sequência de cinco cartas, determine se a sequência dada está ordenada crescentemente, decrescentemente, ou não está ordenada.
Entrada - A entrada consiste de uma única linha que contém as cinco cartas da sequência. Os valores das cartas são representados por inteiros entre 1 e 13. As cinco cartas têm valores distintos.
Saída - Seu programa deve produzir uma única linha, contendo um único caractere maiúsculo: C caso a sequência dada esteja ordenada crescentemente, D se estiver ordenada decrescentemente, ou N caso contrário.'''

cartas = list(map(int, input().split()))
while True: 
    if len(cartas) != 5:
        print("Erro entre com a lista de cartas novamente. Precisa ter 5 cartas!")
        cartas = list(map(int, input().split()))
    elif any(elemento > 13 for elemento in cartas): #não precisa por == True pois é default
        print("Erro, nenhum número pode ser maior que 13!")
        cartas = list(map(int, input().split()))
    else: 
        break

if cartas[0] > cartas[1] and cartas[1] > cartas[2] and cartas[2] > cartas[3] and cartas[3] > cartas[4]:
    print("D")
elif cartas[0] < cartas[1] and cartas[1] < cartas[2] and cartas[2] < cartas[3] and cartas[3] < cartas[4]:
    print("C")
else:
    print("N")
