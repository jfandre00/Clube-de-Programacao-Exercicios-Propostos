#Exemplo 1

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Exemplo de matriz de adjacência
# Este grafo é representado pela matriz de adjacência abaixo:
#    A  B  C  D
# A [0, 1, 1, 0]
# B [1, 0, 1, 0]
# C [1, 1, 0, 1]
# D [0, 0, 1, 0]

matriz_adj = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
])


# Cria um grafo a partir da matriz de adjacência
G = nx.from_numpy_array(matriz_adj)

# Define os nós de partida e chegada
start_node = 0  # Nó A
end_node = 3    # Nó D

# Encontra um caminho simples entre start_node e end_node
try:
    simple_path = nx.shortest_path(G, source=start_node, target=end_node)
    # Converte os nós para letras (opcional)
    nodes_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    simple_path_named = [nodes_map[node] for node in simple_path]
    print("Caminho simples encontrado:", simple_path_named)
except nx.NetworkXNoPath:
    print(f"Não há caminho entre {start_node} e {end_node}")

# Opcional: desenha o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, labels=nodes_map, node_color='lightblue', edge_color='gray')
plt.show()