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

    