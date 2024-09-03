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

'''
1. Introdução ao Problema
Cenário: Estamos trabalhando em uma simulação de um sistema de concursos de programação, como os concursos ACM. A tarefa é processar as submissões de código feitas pelos times e classificá-los de acordo com o número de problemas resolvidos e o tempo total gasto.

Objetivo: Implementar um programa que leia as submissões dos times, calcule a pontuação e o tempo de cada time, e depois classifique os times de acordo com as regras estabelecidas.

2. Entendimento das Regras
Aceitação/Rejeição de Submissões: Cada submissão de um time pode ser aceita (solução correta) ou rejeitada (solução incorreta).

Problemas Resolvidos: Um problema é considerado resolvido por um time se uma das submissões para esse problema for aceita.

Cálculo do Tempo:

Para um problema resolvido, o tempo consumido é o tempo da primeira submissão aceita mais 20 minutos (1200 segundos) para cada submissão anterior rejeitada.
Para problemas não resolvidos, o tempo não é contabilizado.
Critérios de Classificação:

Número de Problemas Resolvidos: Times que resolvem mais problemas ficam melhor classificados.
Tempo Total: Em caso de empate no número de problemas resolvidos, os times são classificados pelo menor tempo total.
Número do Time: Se houver empate no número de problemas resolvidos e no tempo total, o time com o menor número é classificado primeiro.
3. Estrutura do Código
Agora que entendemos as regras, vamos discutir como implementamos a solução.

a) Função Principal: rank_teams
Objetivo: Processar as submissões dos times e calcular a classificação final.

Dicionários Utilizados:

total_time: Armazena o tempo total para cada time.
problems_solved: Armazena o número de problemas resolvidos por cada time.
problem_status: Armazena o status de cada problema para cada time, incluindo o número de tentativas e se o problema foi resolvido.
b) Lógica de Processamento
Para cada submissão, verificamos se o problema já foi resolvido:
Se o problema foi resolvido, ignoramos submissões posteriores para esse problema.
Se a submissão é aceita, calculamos o tempo total (incluindo penalidades por submissões rejeitadas) e marcamos o problema como resolvido.
Se a submissão é rejeitada, apenas aumentamos o contador de tentativas.
c) Ordenação dos Times
Após processar todas as submissões, os times são ordenados:
Primeiro, pelo número de problemas resolvidos (ordem decrescente).
Depois, pelo tempo total (ordem crescente).
Finalmente, pelo número do time (ordem crescente).
'''