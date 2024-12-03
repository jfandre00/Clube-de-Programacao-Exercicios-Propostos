# Entrada de dados
f, r = map(int, input().split())  # Comprimento da fita e número de gotas
posicoes = list(map(int, input().split()))  # Posições das gotas

# Calcula a maior distância que precisa ser percorrida
# 1. Distância inicial à esquerda da primeira gota
max_distancia = posicoes[0] - 1

# 2. Distâncias entre gotas consecutivas
for i in range(1, r):
    distancia = (posicoes[i] - posicoes[i - 1]) // 2
    max_distancia = max(max_distancia, distancia)

# 3. Distância final à direita da última gota
max_distancia = max(max_distancia, f - posicoes[-1])

# Saída do número de dias necessários
print(max_distancia)