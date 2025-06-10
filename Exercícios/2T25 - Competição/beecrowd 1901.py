N = int(input())

# Lê a matriz da floresta
floresta = []
for _ in range(N):
    linha = list(map(int, input().split()))
    floresta.append(linha)

# Conjunto para armazenar espécies únicas
especies = set()

# Lê as 2*N coordenadas visitadas
for _ in range(2 * N):
    x, y = map(int, input().split())
    # As coordenadas são 1-indexadas, então subtrai 1
    especie = floresta[x - 1][y - 1]
    especies.add(especie)

# Imprime a quantidade de espécies únicas coletadas
print(len(especies))
