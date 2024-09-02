# Leitura dos valores de entrada
C, N = map(int, input().split())

# Inicializar a estrutura de dados para armazenar informações dos times
times = {i: {'resolvidos': 0, 'tempo_total': 0, 'submissoes': {}} for i in range(1, C+1)}

# Função para processar uma submissão
def processar_submissao(ci, pi, ti, ri):
    if pi not in times[ci]['submissoes']:
        times[ci]['submissoes'][pi] = {'aceito': False, 'tempo_primeira_aceita': 0, 'tentativas_rejeitadas': 0}
    
    problema = times[ci]['submissoes'][pi]
    
    if ri == 1:  # Submissão aceita
        if not problema['aceito']:
            problema['aceito'] = True
            problema['tempo_primeira_aceita'] = ti
            times[ci]['resolvidos'] += 1
            times[ci]['tempo_total'] += ti + 20 * problema['tentativas_rejeitadas']
    else:  # Submissão rejeitada
        if not problema['aceito']:
            problema['tentativas_rejeitadas'] += 1

# Processar cada submissão
for _ in range(N):
    ci, pi, ti, ri = map(int, input().split())
    processar_submissao(ci, pi, ti, ri)

# Ordenar os times de acordo com as regras
rank = sorted(times.keys(), key=lambda x: (-times[x]['resolvidos'], times[x]['tempo_total'], x))

# Imprimir os números dos times na ordem correta
print(' '.join(map(str, rank)))