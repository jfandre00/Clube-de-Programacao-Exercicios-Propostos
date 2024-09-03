def rank_teams(C, N, runs):
    #Dicionário para armazenar o tempo total e problemas resolvidos para cada time
    total_time = {i: 0 for i in range(1, C+1)}
    problems_solved = {i: 0 for i in range(1, C+1)}
    problem_status = {i: {} for i in range(1, C+1)}

    for ci, pi, ti, ri in runs:
        if pi not in problem_status[ci]:
            problem_status[ci][pi] = {'attempts': 0, 'solved': False, 'time': 0}

        if not problem_status[ci][pi]['solved']:
            if ri == 1:  # Se o problema é aceito
                problems_solved[ci] += 1
                #O tempo que levou é o tempo atual mais 20 minutos (1200 segundos) por tentativa errada
                problem_status[ci][pi]['time'] = ti + problem_status[ci][pi]['attempts'] * 1200
                total_time[ci] += problem_status[ci][pi]['time']
                problem_status[ci][pi]['solved'] = True
            else:  # Se o problema é rejeitado
                problem_status[ci][pi]['attempts'] += 1

    # Fazer a lista para ordenar os times
    teams = [(ci, problems_solved[ci], total_time[ci]) for ci in range(1, C+1)]

    # Ordenar os times pelo número de problemas resolvidos (decrescente), depois pelo tempo total (crescente), depois pelo número do time
    teams.sort(key=lambda x: (-x[1], x[2], x[0]))

    # Extrair os números dos times ordenados
    result = [team[0] for team in teams]
    return result

# Leitura da entrada
C, N = map(int, input().split())
runs = [tuple(map(int, input().split())) for _ in range(N)]

# Chama a função e imprime o resultado
result = rank_teams(C, N, runs)
print(" ".join(map(str, result)))