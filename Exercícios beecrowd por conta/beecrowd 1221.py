# beecrowd 1221 - Números Primos


import math

def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

testes = int(input())
for i in range(testes):
    n = int(input())
    if eh_primo(n):
        print('Prime')
    else:
        print('Not Prime')

#Solução abaixo deu time limit exceeded
'''def eh_primo(n):
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False
    return True



testes = int(input())
for i in range(testes):
    n = int(input())
    if eh_primo(n):
        print('Prime')
    else:
        print('Not Prime')'''