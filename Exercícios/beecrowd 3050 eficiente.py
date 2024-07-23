'''

solução mais eficiente e aceita pelo beecrowd

Como resolver de forma mais eficiente, sem precisar calcular todas as distâncias?

encontrar o melhor prédio da esquerda e o melhor prédio da direita
considerando o prédio mais alto da esquerda que gera a maior distância, e o mesmo à direita

diferença do prédio 1 = altura do prédio 1 - distância da ponta esquerda
d = 2 - (1 - 1) = 2

diferença do prédio 4 = altura prédio 4 - distância do prédio 4 até a ponta esquerda => 6 - (4 - 1) = 3

faz para todos os prédios até o penúltimo

faz a mesma coisa para encontrar o melhor da direita

diferença do ultimo prédio = altura do ultimo prédio - distância da ponta direita

distância do prédio 11 = 5 - (14  - 11) = 2
a conta vai até o prédio fixo a esquerda, que já foi determinado acima

dist (4, 11) = 6 + 5 + (8 -1) = 18
'''

n = int(input())
andares = [int(a) for a in input().split()]

e = 0

for i in range(1, n-1):
    if andares[i] - i > andares[e] -e:
        e = i

d = -1 
for i in range(-2, e - n, -1):
    if andares[i] + i > andares[d] +d:
        d = i

print(andares[e] + andares[d] + d + n - e)
