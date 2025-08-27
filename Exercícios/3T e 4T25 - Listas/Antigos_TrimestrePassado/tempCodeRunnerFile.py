n, v = map(int, input().split())

melhor_tempo = None
piloto_melhor_volta = None
classificacao = {}

for _ in range(n):
    dados = input().split()
    piloto = int(dados[0])
    voltas = []

    for tempo_str in dados[1:]:
        m, s, ms = map(int, tempo_str.split(':'))
        total_ms = m * 60000 + s * 1000 + ms
        voltas.append(total_ms)

        # Atualiza melhor volta
        if melhor_tempo is None or total_ms < melhor_tempo:
            melhor_tempo = total_ms
            piloto_melhor_volta = piloto
        # Se for igual, não troca (garante que o primeiro fica)

    # Salva tempo total para classificação
    classificacao[piloto] = sum(voltas)

# Ordena por menor tempo total
classificacao_ordenada = sorted(classificacao.items(), key=lambda x: x[1])

# Verifica se o piloto da melhor volta está no top 10
top_10_pilotos = [p for p, _ in classificacao_ordenada[:10]]

if piloto_melhor_volta in top_10_pilotos:
    print(piloto_melhor_volta)
else:
    print("NENHUM")