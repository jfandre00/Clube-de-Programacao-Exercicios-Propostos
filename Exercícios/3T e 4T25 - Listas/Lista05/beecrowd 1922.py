n, m = map(int, input().split())
# exemplo: di = 4 e kdi = 16 -> aparece em: 4,8,12,16

aparicoes = []
maior_instante = 0

for _ in range(n):
    di, kdi = map(int, input().split())

    instantes = []
    t = di

    # Gera todos os instantes q a criatura aparece
    while t <= kdi:
        instantes.append(t)
        t += di

    aparicoes.append(instantes)

    # Maior instante observado dentre todas as criaturas
    if kdi > maior_instante:
        maior_instante = kdi

# Lista para saber quais criaturas aparecem (1 por segundo até o maior instante)
tempo_para_criaturas = [[] for _ in range(maior_instante + 1)]

# vamos preecher a lista
for indice_criatura, instantes in enumerate(aparicoes):
    for t in instantes:
        tempo_para_criaturas[t].append(indice_criatura)


# Criaturas já marteladas não aparecem mais, então usarei um set 
atingidas = set()

# A cada martelada vamos escolher o instante que atinge a MAIOR qtde de criaturas que ainda não foram marteladas

for _ in range(m):  #  até m marteladas

    melhor_tempo = -1    # -1 para indicar que não achamos nenhum ainda
    melhor_qtd = 0       # quantas criaturas novas podemos acertar

    for t in range(1, maior_instante + 1):

        criaturas_no_instante = tempo_para_criaturas[t]

        # Apenas as criaturas que ainda não foram marteladas
        ainda_nao_atingidas = [c for c in criaturas_no_instante if c not in atingidas]

        # Ver quantas novas criaturas poderíamos acertar agora
        qtd = len(ainda_nao_atingidas)

        # Teste se é a melhor opção até agora
        if qtd > melhor_qtd:
            melhor_qtd = qtd
            melhor_tempo = t

    # Se não conseguimos atingir nenhuma criatura nova, paramos
    if melhor_qtd == 0:
        break

    # Martelamos no melhor instante encontrado
    # Vamos marcar todas as criaturas daquele instante como já atingidas.
    for c in tempo_para_criaturas[melhor_tempo]:
        atingidas.add(c)

print(len(atingidas))
