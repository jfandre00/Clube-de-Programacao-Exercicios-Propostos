import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Definir arestas (u, v) do triângulo
edges = [
    (0, 1),  # Aresta entre nós 1 e 2
    (1, 2),  # Aresta entre nós 2 e 3
    (2, 0)   # Aresta entre nós 3 e 1
]

# Número de nós e arestas
num_nodes = 3
num_edges = len(edges)

# Matriz de incidência
incidence_matrix = np.zeros((num_nodes, num_edges), dtype=int)

# Preencher a matriz de incidência
for idx, (u, v) in enumerate(edges):
    incidence_matrix[u, idx] = 1
    incidence_matrix[v, idx] = 1

# Nós (opcional, para atribuir rótulos aos nós)
nodes = ['1', '2', '3']

# Criar um grafo não ponderado a partir das arestas
G = nx.Graph()
G.add_edges_from(edges)

# Configurações de plotagem
pos = nx.spring_layout(G)  # Layout para organizar os nós

# Plotar o grafo
nx.draw(G, pos, with_labels=True, labels=dict(enumerate(nodes)), node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
plt.title('Triângulo Representado por Matriz de Incidência')
plt.show()

# Exibir a matriz de incidência
print("Matriz de Incidência:")
print(incidence_matrix)