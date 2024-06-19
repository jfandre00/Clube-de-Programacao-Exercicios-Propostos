# Leitura da entrada - beecrowd 2832 - correto porem sem busca binária
N, F = map(int, input().split())
ciclos = list(map(int, input().split()))

# Inicialização das variáveis
total_moedas = 0
dia = 0

# Loop até acumular pelo menos F moedas
while total_moedas < F:
    dia += 1
    for ciclo in ciclos:
        if dia % ciclo == 0:
            total_moedas += 1

# Imprime o resultado
print(dia)