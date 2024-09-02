#beecrowd 5019
'''
1 - Ler o número de hóspedes N.
2 - Ler as listas de tempos de chegada e partida.
3 - Criar uma lista de eventos, onde cada evento é uma tupla (tempo, tipo), onde tipo é 1 para chegada e -1 para partida.
4 - Ordenar a lista de eventos. Em caso de empate, partidas (-1) devem vir antes de chegadas (1).
5 - Iterar sobre a lista de eventos, mantendo um contador de hóspedes atuais e atualizando o máximo de hóspedes simultâneos.'''

N = int(input())
chegadas = list(map(int, input().split()))
partidas = list(map(int, input().split()))

eventos = []
for i in range(N):
    eventos.append((chegadas[i], 1))  # Evento de chegada
    eventos.append((partidas[i], -1))  # Evento de partida

# Ordenar eventos: primeiro por tempo, depois por tipo (partidas antes de chegadas em caso de empate)
eventos.sort(key=lambda x: (x[0], x[1]))

max_hospedes = 0
hospedes_atuais = 0

for evento in eventos:
    hospedes_atuais += evento[1]
    if hospedes_atuais > max_hospedes:
        max_hospedes = hospedes_atuais

print(max_hospedes)