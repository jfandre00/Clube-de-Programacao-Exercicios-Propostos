# Leitura da entrada - beecrowd 2832 solução aceita
N, F = map(int, input().split())
ciclos = list(map(int, input().split()))

# Inicialização das variáveis para a busca binária
esquerda, direita = 1, 10**8

# Função para calcular quantas moedas são produzidas em 'dias' dias
def moedas_produzidas_em(dias):
    return sum(dias // ciclo for ciclo in ciclos)

# Loop da busca binária
while esquerda < direita:
    meio = (esquerda + direita) // 2
    if moedas_produzidas_em(meio) >= F:
        direita = meio  # Pode ser uma solução viável
    else:
        esquerda = meio + 1  # Precisamos de mais dias

# Imprime o resultado
print(esquerda)