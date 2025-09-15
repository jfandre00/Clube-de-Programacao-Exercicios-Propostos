# Primeiro caso de teste (fora do loop)
players, quadrados = map(int, input().split())

while players != 0 and quadrados != 0:
    armadilhas_input = map(int, input().split())
    armadilhas = set(armadilhas_input) # set é mais rápido para verificar se um número existe
    
    rolagem_dados = int(input())
    jogadas = []
    for _ in range(rolagem_dados):
        dado1, dado2 = map(int, input().split())
        jogadas.append(dado1 + dado2)
    
    posicao_jogadores = [0] * players  # Posição inicial de cada jogador
    proxima_vez_perde = [False] * players # Para saber se o jogador deve pular a vez
    
    jogador_atual = 0
    indice_jogada = 0 # Índice para controlar qual jogada usar
    vencedor_encontrado = False

    while not vencedor_encontrado:
        # Verifica se o jogador atual deve pular a vez
        if proxima_vez_perde[jogador_atual]:
            proxima_vez_perde[jogador_atual] = False
            # O jogador pula a vez, mas a jogada não é consumida. O 'indice_jogada' não é incrementado.
        else:
            # O jogador joga normalmente
            soma_dados = jogadas[indice_jogada]
            posicao_jogadores[jogador_atual] += soma_dados
            
            # O índice da jogada só avança se alguém realmente jogou
            indice_jogada += 1
            
            # Verificando se o jogador venceu
            if posicao_jogadores[jogador_atual] > quadrados:
                print(jogador_atual + 1)
                vencedor_encontrado = True
                # continue (para sair do loop while imediatamente após encontrar o vencedor)
                continue
            
            # Verifica se caiu em uma armadilha
            if posicao_jogadores[jogador_atual] in armadilhas:
                proxima_vez_perde[jogador_atual] = True

        # Agora a vez é do próximo jogador, independentemente de ele ter jogado ou pulado
        jogador_atual = (jogador_atual + 1) % players

    # Próximo caso de teste (até encontrar 0 0)
    players, quadrados = map(int, input().split())