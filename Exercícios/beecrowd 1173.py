'''Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

Entrada
A entrada contém um valor inteiro (V<=50).

Saída
Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.'''

'''valor = int(input())
N = [0] * 10 # Inicializa a lista N com 10 elementos

for c in range(11):
    N[c] = valor
    print(f'N[{c}] = {valor}')
    valor *= 2'''

valor = int(input())
N = []

for c in range(10):
    N.append(valor)
    print(f'N[{c}] = {valor}')
    valor *= 2


