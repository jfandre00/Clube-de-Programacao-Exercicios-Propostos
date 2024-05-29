'''
Entrada
A primeira linha consiste em um inteiro C que representa a quantidade de casos de teste. Cada caso de teste é composto por dois inteiros N e M que indicam o tamanho da avenida e a área de cobertura do radar.

(1 ≤ N ≤ 10^9)

(1 ≤ M ≤ 10^9)

Saída
Seu programa deve exibir a menor quantidade de radares necessários para cobrir toda avenida.
'''

C = int(input())


for _ in range(C):
  valores = input().split()
  N = int(valores[0])
  M = int(valores[1])
  if N % M == 0:
    print(N//M)
  else:
    print((N//M)+1)