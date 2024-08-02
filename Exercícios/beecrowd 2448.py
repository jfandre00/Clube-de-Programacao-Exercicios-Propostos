#A SOLUÇÃO ABAIXO FICOU EM 1 SEGUNDO E NÃO FOI ACEITA POR TEMPO EXCEDIDO, ALTERAÇÃO FEITA ABAIXO

'''N, M = map(int, input().split())
casas = list(map(int, input().split()))
encomendas = list(map(int, input().split()))

#casas = [50, 80, 100]
#encomendas = [80, 80, 100, 50]



#Entrega 1
#a = abs(casas.index(casas[0]) - casas.index(encomendas[0]))
#total = abs(casas.index(encomendas[0]))



#for e in range(0, (len(encomendas)-1)):
##for e in range(0, (N-1)):
    total += abs(casas.index(encomendas[e]) - casas.index(encomendas[e+1]))

print(total)'''


'''#entrega 2
total += abs(casas.index(encomendas[0]) - casas.index(encomendas[1]))

#entrega 3
total += abs(casas.index(encomendas[1]) - casas.index(encomendas[2]))

#entrega 4
total += abs(casas.index(encomendas[2]) - casas.index(encomendas[3]))

#entrega 5
total += abs(casas.index(encomendas[3]) - casas.index(encomendas[4]))'''


'''Pesquisa por conta do erro ->  Um erro de "Time limit exceeded" geralmente indica que o algoritmo não é eficiente o suficiente para lidar com o tamanho do input dentro do tempo permitido. Nesse caso, a ineficiência vem do uso do método index dentro de um loop, o que tem uma complexidade de tempo O(N) para cada chamada. Isso resulta em uma complexidade total de O(N^2), que não é viável para tamanhos de entrada grandes.
Para otimizar isso, é melhor criar um dicionário para armazenar os índices de cada casa. Dessa forma, o índice de uma casa será encontrado em tempo constante O(1). '''


#SOLUÇÃO ACEITA PELO BEECROWD, ao invés de verificar o índice em todos os for (linha 53), coloquei dentro de um dicionário já o número do índice

N, M = map(int, input().split())
casas = list(map(int, input().split()))
encomendas = list(map(int, input().split()))

# criei um dicionário para guardar o indice de cada casa
indices = {casa: indice for indice, casa in enumerate(casas)}

print(indices)

# calculo da primeira entrega, pois sempre sai da primeira casa
total = abs(indices[encomendas[0]])

# calculo da distancia total somando o absoluto da diferença dos índices
for e in range(M - 1):
    total += abs(indices[encomendas[e]] - indices[encomendas[e + 1]])

print(total)