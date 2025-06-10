########################## CORRIGIR ESTÀ ERRADPO ##########################

n, v = map(int, input().split())
qualificacao = []
voltaMaisRapida = None
numeroVoltaMaisRapida = None

for i in range(n):
    # leitura dos dados: numeroPiloto é int e tempoVoltas é uma lista de strings, quantidade depende de v
    entrada = input().split()
    numeroPiloto = int(entrada[0])
    tempoVoltas = entrada[1:v+1]
    tempoTotal = 0
    for tempo in tempoVoltas:
        minutos, segundos, milesimos = map(int, tempo.split(':'))
        tempoMilesimos = minutos * 60000 + segundos * 1000 + milesimos
        tempoTotal += tempoMilesimos
        if voltaMaisRapida is None or tempoMilesimos < voltaMaisRapida:
            voltaMaisRapida = tempoMilesimos
            numeroVoltaMaisRapida = numeroPiloto
    qualificacao.append((numeroPiloto, tempoTotal))

#odernar a lista de tempos
qualificacao.sort(key=lambda x: x[1])


# o piloto ganha 1 ponto extra se fez a volta mais rápida, mas precisa ter terminado entre os 10 primeiros


# Verifica se o piloto da volta mais rápida está entre os 10 primeiros
top10_pilotos = [qualificacao[i][0] for i in range(min(10, len(qualificacao)))]

# Procura o primeiro piloto do top 10 que fez a volta mais rápida
primeiro_piloto_volta_mais_rapida = None
for piloto, tempoTotal in qualificacao:
    if piloto in top10_pilotos:
        # Como processamos os dados antes, o primeiro que tiver o tempo igual ao da volta mais rápida é o correto
        # Precisamos reprocessar os tempos das voltas desse piloto
        # Para isso, precisamos armazenar os tempos das voltas na lista qualificacao durante a leitura
        # Mas como não temos, vamos simplificar: basta lembrar que o primeiro piloto que atingiu voltaMaisRapida já está em numeroVoltaMaisRapida
        if piloto == numeroVoltaMaisRapida:
            primeiro_piloto_volta_mais_rapida = piloto
            break

if primeiro_piloto_volta_mais_rapida is not None:
    print(primeiro_piloto_volta_mais_rapida)
else:
    print("NENHUM")
