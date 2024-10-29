from math import comb

#Representa o grid como uma matriz N x M onde 1 é a parede e 0 é espaço livre

n, m = (int(d) for d in input().split())
grid = []
for _ in range(n):
    linha = input()
    grid.append([1 if c == '#' else 0 for c in linha])

while True:
    try:
        #Lê as coordenadas do retângulo
        xa, ya, xb, yb = (int(d) for d in input().split())

        #Calcula o total de células no retângulo
        celulas = (xb - xa + 1) * (yb - ya + 1)

        #Conta o número de paredes no retângulo
        paredes = 0
        for l in range(xa - 1, xb):
            for c in range(ya - 1, yb):
                paredes += grid[l][c]
        
        #Usa a função comb para calcular o número de possibilidades
        possibilidades = (comb(celulas, paredes) -1) % 1000000007

        #Imprime o resultado
        print(possibilidades)

    except EOFError:
        break
    