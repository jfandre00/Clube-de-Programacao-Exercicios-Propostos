# Pão de Queijo Sweeper - fazendo pela segunda vez, agora sem usar o colchão de zeros ao redor

# Vizinhos diretos: cima, baixo, esquerda, direita
vizinhos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    try:
        linhas, colunas = map(int, input().split())
        tabuleiro = [list(map(int, input().split())) for _ in range(linhas)]

        resultado = [[0] * colunas for _ in range(linhas)]  # para armazenar o resultado

        for linha in range(linhas):
            for coluna in range(colunas):
                if tabuleiro[linha][coluna] == 1:  # se for um pão de queijo, marca com 9
                    resultado[linha][coluna] = 9
                else:
                    total_paes = 0
                    for deslocamento_linha, deslocamento_coluna in vizinhos: # verifica os vizinhos, fará 4 iterações para cada célula (de acordo com a lista vizinhos)
                        nova_linha = linha + deslocamento_linha
                        nova_coluna = coluna + deslocamento_coluna
                        if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas: # verifica se está dentro dos limites
                            if tabuleiro[nova_linha][nova_coluna] == 1: # se for um pão de queijo
                                total_paes += 1  # conta o pão de queijo
                    resultado[linha][coluna] = total_paes  # atualiza o resultado com o total de pães de queijo ao redor

        # imprimir na tela o tabuleiro completo
        for linha in resultado:
            print("".join(map(str, linha)))

    except EOFError:
        break
