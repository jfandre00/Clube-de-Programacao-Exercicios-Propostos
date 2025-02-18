#beecrowd 1266

#cerca temporária -> serão colocados nos mesmos pontos onde os postes estão faltando, mas irão utilizar menos poste. 
#1 poste de madeira será utilizado somente se a distância entre os postes for superior a 4 metros.
#dada a descrição de quantos postes estão quebrados ou faltando, você deve escrever um programa que determine
#a menor quantidade de postes de madeira que serão necessários para fechar as lacunas da cerca, de acordo com
#a decisão dos proprietários. Originalmente a distância entre os postes é de 2 metros.
#Entrada - vários casos de teste. Primeira Linha N -> número original de postes (5 a 5000)
#Segunda linha -> N inteiros (0 ou 1) representando a situação dos postes. 1 -> poste em boas condições, 0 -> poste danificado
#O poste N fica ao lado do poste 1. é um circuito fechado.

#Saída - para cada caso de teste, imprima um número inteiro representando a menor quantidade de postes de madeira que serão necessários para fechar as lacunas da cerca.

'''
Exemplo de entrada:
10
1 0 0 1 0 0 1 0 1 1 - saída 2
11 
1 0 0 1 0 0 0 1 1 0 1 - saída 2
12
0 0 0 0 0 1 1 0 0 0 1 1 - saída 3
'''

#Usando o exemplo 1
#subtrair a posição no array de postes bons para saber a distância entre eles - distância entre poste 0 e 3 = 3 posições, que ultrapassa o limite de 2 (4 metros) -> Basta adicionar 1 poste de madeira
#distância entre poste 3 e 6 = 3 posições, que ultrapassa o limite de 2 (4 metros) -> Basta adicionar 1 poste de madeira
#distância entre postes 6 e 8 = 2 posições, que não ultrapassa o limite de 2 (4 metros) -> Não é necessário adicionar poste de madeira
#distância entre postes 8 e 9 = 1 posição, que não ultrapassa o limite de 2 (4 metros) -> Não é necessário adicionar poste de madeira
#distância entre postes 9 e 0 = 1 posição, que não ultrapassa o limite de 2 (4 metros) -> Não é necessário adicionar poste de madeira

#resumo: pegar as posições dos postes bons, calcular a distância entre eles e verificar se a distância ultrapassa 4 metros. 

# P = [(D-1) / 2] - onde P é o número de postes de madeira necessários e D é a distância entre os postes bons, arredondando para baixo quando o resultado não for inteiro.

import math

while True:
    try:
        # Lê o valor de N (nº original de postes)
        n = int(input())
        if n == 0:
            break

        # Lê estado de cada poste na cerca (0=danificado, 1=bom)
        cerca = input().split()

        # Cria array com posições dos postes bons
        bons = [i for i in range(n) if cerca[i] == '1']

        postes = 0
        if len(bons) == 0:
            postes += math.ceil(n / 2)
        else:
            for i in range(len(bons) - 1):
                # Calcula distância entre postes bons
                dist = bons[i+1] - bons[i]
                postes += (dist - 1) // 2
            dist = n - bons[-1] + bons[0]
            postes += (dist - 1) // 2

        # Imprime a saída
        print(postes)

    except EOFError:
        break