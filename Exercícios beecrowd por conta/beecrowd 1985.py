p = int(input())
pedido = []
precos = [1.5, 2.5, 3.5, 4.5, 5.5]
primeiro_codigo = 1001
total = 0

for order in range(p):
    codigo, qtdade = map(int, input().split())
    total += qtdade * precos[codigo-primeiro_codigo]


print(f'{total:.2f}')