def rank_teams(C, N, submissions):
    from collections import defaultdict
    
    # Informações das equipes
    teams = defaultdict(lambda: {'solved': 0, 'time': 0, 'problems': defaultdict(list)})
    
    # Processamento das submissões
    for ci, pi, ti, ri in submissions:
        teams[ci]['problems'][pi].append((ti, ri))
    
    # Cálculo dos tempos e problemas resolvidos
    for team in teams:
        for problem in teams[team]['problems']:
            attempts = sorted(teams[team]['problems'][problem])  # Ordena tentativas pelo tempo
            time_penalty = 0
            solved = False
            for time, result in attempts:
                if result == 1:  # Aceito
                    teams[team]['solved'] += 1
                    teams[team]['time'] += time + time_penalty
                    solved = True
                    break
                else:  # Rejeitado
                    time_penalty += 1200  # 20 minutos (1200 segundos)
    
    # Ordenação das equipes conforme as regras
    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]['solved'], x[1]['time'], x[0]))
    
    # Retorno dos times ordenados
    return [team[0] for team in sorted_teams]

# Leitura de dados de entrada
C, N = map(int, input().split())
submissions = [tuple(map(int, input().split())) for _ in range(N)]

# Calculando e imprimindo a classificação
ranking = rank_teams(C, N, submissions)
print(" ".join(map(str, ranking)))