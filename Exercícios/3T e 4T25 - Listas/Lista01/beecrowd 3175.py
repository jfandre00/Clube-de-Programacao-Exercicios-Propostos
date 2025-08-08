list_boas_acoes = []
dictionary_boas_acoes = {}
quantidade_de_presentes = 0

n = int(input())
list_boas_acoes = list(map(int, input().split()))

for acao in list_boas_acoes:
    if acao not in dictionary_boas_acoes:
        dictionary_boas_acoes[acao] = 1
    else:
        dictionary_boas_acoes[acao] += 1

# Ordenar o dicionário pelas chaves
dictionary_boas_acoes = dict(sorted(dictionary_boas_acoes.items()))

# lista de chaves ordenadas fora do loop pois deu time limit exceeded
chaves_ordenadas = list(dictionary_boas_acoes.keys())
for idx, acao in enumerate(chaves_ordenadas):
    # vamos usar o índice do loop diretamente, evitando .index() dentro do loop
    quantidade_de_presentes += (idx + 1) * dictionary_boas_acoes[acao]

# for acao in dictionary_boas_acoes.keys():
#     #precisamos pegar o indice no dicionario, somar 1 (pois começa em zero) e multiplicar pelo numero de ocorrencias
#     quantidade_de_presentes += (list(dictionary_boas_acoes.keys()).index(acao) + 1) * dictionary_boas_acoes[acao]

print(quantidade_de_presentes)
