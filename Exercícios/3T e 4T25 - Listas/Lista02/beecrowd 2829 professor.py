n = int(input())

# vamos pegar as palavras, colocar em minusculas e concatenar com a string original, e depois ordenar

palavras = []
for _ in range(n):
    p = input()
    palavras.append(p.lower() + p)

palavras.sort()

for p in palavras:
    print(p[len(p) // 2:]) # estou peganndo a partir do meio da string, que é onde começa a palavra original até o final dela

'''
for palavra in palavras:
    inicio_corte = len(palavra) // 2
    fim_corte = len(palavra)
    print(palavra[inicio_corte:fim_corte])
'''