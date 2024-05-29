'''
O sistema de numeração duotrigesimal é composto de 32 algarismos (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V).
o numero 31 é V
o número 32 é 10
'''


BASE = 32
a = []
base32 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']

 
n = int(input())
for _ in range(n):
  if n // BASE != 0:
    a.append(n % BASE)
    n = n // BASE
  else:
    a.append(n % BASE)
    break

#exercicio beecrowd 1869
#converter para os números de A a V
#testes de validacao 1300 = 1 8 20
#testes de validacao 0 = 0
#testes de validacao 1024 = 1 0 0 
if n == 0:
  a.append(0)
a.reverse()

for i in a:
  print(base32[i], end='')
