# Lê o número de palavras usando a função padrão input().
num_palavras = int(input())

# Cria uma lista para armazenar todas as palavras.
# Usar uma list comprehension é uma forma "pythônica" e eficiente de fazer isso.
palavras = [input() for _ in range(num_palavras)]

# O ponto principal da solução: ordenar a lista.
# A lógica é a mesma da solução anterior.
# Usamos uma função lambda como chave de ordenação.
# Para cada palavra 'p', a chave é uma tupla: (p.lower(), p).
# 1. Python primeiro ordena com base em p.lower() (ordem alfabética case-insensitive).
# 2. Se houver um empate (ex: 'Abc'.lower() == 'abc'.lower()),
#    Python usa o segundo elemento da tupla, 'p' (a palavra original),
#    para desempatar. Na comparação padrão de strings, 'A' < 'a',
#    então 'Abc' virá antes de 'abc'.
palavras.sort(key=lambda p: (p.lower(), p))

# Imprime a lista ordenada, cada palavra em uma nova linha.
for palavra in palavras:
    print(palavra)

