def resultado_jogo(g1, g2):
    """Retorna 1 se time1 venceu, -1 se time2 venceu, 0 se empate."""
    if g1 > g2:
        return 1
    elif g1 < g2:
        return -1
    return 0

while True:
    participantes, numero_partidas = map(int, input().split())
    if participantes == 0 and numero_partidas == 0:
        break  # fim da entrada

    palpites = {}
    nomes = []

    # Lendo palpites
    for _ in range(participantes):
        nome = input().strip()
        nomes.append(nome)
        palpites[nome] = []
        for _ in range(numero_partidas):
            time1, g1, time2, g2 = input().split()
            g1, g2 = int(g1), int(g2)
            palpites[nome].append((time1, g1, time2, g2))

    # Lendo resultados reais
    resultados = []
    for _ in range(numero_partidas):
        time1, g1, time2, g2 = input().split()
        g1, g2 = int(g1), int(g2)
        resultados.append((time1, g1, time2, g2))

    # Calculando pontuação
    pontuacao = {}
    for nome in nomes:
        pontos = 0
        for i in range(numero_partidas):
            time1_p, g1_p, time2_p, g2_p = palpites[nome][i]
            time1_r, g1_r, time2_r, g2_r = resultados[i]

            # Resultado (vitória/empate)
            res_palpite = resultado_jogo(g1_p, g2_p)
            res_real = resultado_jogo(g1_r, g2_r)

            if g1_p == g1_r and g2_p == g2_r:
                pontos += 10
            elif res_palpite == res_real and (g1_p == g1_r or g2_p == g2_r):
                pontos += 7
            elif res_palpite == res_real:
                pontos += 5
            elif g1_p == g1_r or g2_p == g2_r:
                pontos += 2
            # else: 0 pontos
        pontuacao[nome] = pontos

    # Ordenar: pontuação desc, nome asc
    ranking = sorted(pontuacao.items(), key=lambda x: (-x[1], x[0]))

    # Imprimir ranking
    for nome, pontos in ranking:
        print(f"{nome} {pontos}")

