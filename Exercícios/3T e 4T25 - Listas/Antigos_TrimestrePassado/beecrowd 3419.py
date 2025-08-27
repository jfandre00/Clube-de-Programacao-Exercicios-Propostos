n, v = map(int, input().split())

best_lap = None         # melhor tempo de volta (ms)
best_pilot = None       # piloto que fez essa volta
best_completion = None  # tempo acumulado até essa volta (ms) — desempate

totals = {}  # {piloto: tempo_total_ms}

for _ in range(n):
    dados = input().split()
    piloto = int(dados[0])
    acc = 0
    totals[piloto] = 0

    for tempo_str in dados[1:]:
        m, s, ms = map(int, tempo_str.split(':'))
        lap = m * 60000 + s * 1000 + ms
        acc += lap
        totals[piloto] += lap

        # Atualiza melhor volta com regra de desempate pelo tempo acumulado
        if (best_lap is None
            or lap < best_lap
            or (lap == best_lap and acc < best_completion)):
            best_lap = lap
            best_pilot = piloto
            best_completion = acc

# Ordena por menor tempo total e pega top 10
classificados = sorted(totals.items(), key=lambda x: x[1])
top10 = {p for p, _ in classificados[:10]}

print(best_pilot if best_pilot in top10 else "NENHUM")
