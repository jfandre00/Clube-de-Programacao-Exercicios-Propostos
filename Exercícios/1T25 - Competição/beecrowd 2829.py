# lista de palavras que podem ter minuscúlas e maiúsculas de a até z ou A até Z
# precisamos ordenar, obedecendo a mesma ordem de entrada, mas sem diferenciar maiúsculas de minúsculas

# para desempatar depois que todas as letrar forem comparadas, considerar que maiúsculas vem antes de minúsculas

# entrada
#4
#Abcd
#zbcd
#zBce
#abzd

# saída
#Abcd
#abzd
#zbcd
#zBce

n = int(input())

palavras = []
for i in range(n):
    palavras.append(input())

palavras.sort(key=lambda x: (x.lower(), x)) # ordena as palavras, ignorando a diferença entre maiúsculas e minúsculas e depois ordena pela palavra original

for palavra in palavras:
    print(palavra)


