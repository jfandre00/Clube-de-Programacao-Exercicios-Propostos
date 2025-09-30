largura = int(input().strip())
altura = int(input().strip())

mapa = [input().rstrip("\n") for _ in range(altura)] # ler o mapa de uma vez, sem espaços extras

# dicionário de movimentos possíveis para cada direção
direcoes = {
    '>': (0, 1),   # direita
    '<': (0, -1),  # esquerda
    'v': (1, 0),   # baixo
    '^': (-1, 0)   # cima
}

# Aonde vamos começar
linha = 0
coluna = 0

# Primeiro movimento (para a direita)
mov_linha = 0 
mov_coluna = 1

# Para detectar loops, já que o set não permite duplicatas
visitados = set()

while True:
    # Fora do mapa - movimento inválido
    if not (0 <= linha < altura and 0 <= coluna < largura):
        print("!")
        break

    celula = mapa[linha][coluna]

    # Achou baú - movimento válido
    if celula == "*":
        print("*")
        break

    # Entrou no loop
    estado = (linha, coluna, mov_linha, mov_coluna)
    if estado in visitados:
        print("!")
        break
    visitados.add(estado)

    # Se for seta, muda a direção
    if celula in direcoes:
        mov_linha, mov_coluna = direcoes[celula]

    # Avança um passo
    linha += mov_linha
    coluna += mov_coluna