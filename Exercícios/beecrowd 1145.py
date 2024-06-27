#beecrowd 1445

#Leitura do número N, só para quando digita zero
N = int(input("Digite o número N: "))

while N != 0:
    #Inicializar uma lista para armazenar as relações
    relacoes = []

    #Ler as N relações
    entrada = input("Digite as relações (separadas por espaço): ")
    pares = entrada.split(' ')

    #Transformar cada string no formato (x,y) em uma tupla (x, y). Serão armazenadas dentro da lista relações
    for par in pares:
        x, y = par.strip('()').split(',')
        relacoes.append((int(x), int(y)))

    #Criar um grafo a partir das relações (grafo árvore) Usamos o dicionário para representar o grafo onde cada chave é um nó (convidado) e o valor é uma lista de nós adjacentes (convidados relacionados)
    grafo = {}
    for x,y in relacoes:
        if x not in grafo:
            grafo[x] = []
        if y not in grafo:
            grafo[y] = []
        grafo[x].append(y)
        grafo[y].append(x)

    #Usar BFS (Breadth-First-Search, busca em largura) para encontrar todos os convidados a partir do anfitrião (número 1) - Percorre todosos convidados que podem ser alcançados a partir do anfitrião (número 1). Apenas os convidados alcançáveis são contados.
    #Um set armazena coleções de elementos únicos
    visitados = set()
    fila = [1] #Usando uma lista simples como fila, começa com 1 que é o anfitrião
    while fila:
        convidado = fila.pop(0) #Remove o primeiro item da lista
        if convidado not in visitados:
            visitados.add(convidado)
            if convidado in grafo:
                for vizinho in grafo[convidado]:
                    if vizinho not in visitados:
                        fila.append(vizinho)
    
    #Imprimir o número de convidados (incluindo o anfitrião)
    print(len(visitados))

    #Leitura do próximo número N
    N = int(input("Digite o número N: "))
