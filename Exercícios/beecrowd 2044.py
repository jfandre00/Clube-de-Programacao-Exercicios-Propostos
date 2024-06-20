'''while True:
    soma_valores = 0
    N = int(input("Entre com o número de museus: "))
    if N == -1:
        break
    lista = []
    for c in range (1,N+1):
        Pi = int(input(f'entre com {c}º número: '))
        lista.append(Pi)
        soma_valores += Pi
    print(soma_valores//100)'''

while True:
    N = int(input())
    if N == -1:
        break
    prices = list(map(int, input().split()))
    
    debt = 0
    visits = 0
    
    for price in prices:
        debt += price
        if debt % 100 == 0:
            visits += 1
            debt = 0
    
    print(visits)

"""

Solução do professor em aula no dia 20-06-24
n = int(input())
while n != -1:
    p = [int(num) for num in input().split()]
    divida = 0
    visitas = 0
    for preco in p:
        divida += preco
        if divida % 100 == 0:
            visitas += 1
            debito = 0
    
    print(visitas)
    n = int(input())
            
"""