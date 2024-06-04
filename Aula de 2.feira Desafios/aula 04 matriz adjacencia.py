import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# Matriz de adjacência
adjacency_matrix = np.array([
 [0, 1, 1, 0, 0],
 [1, 0, 1, 1, 0],
 [1, 1, 0, 1, 1],
 [0, 1, 1, 0, 1],
 [0, 0, 1, 1, 0]
])
# Nós (opcional, para atribuir rótulos aos nós)
nodes = ['A', 'B', 'C', 'D', 'E']
# Criar um grafo não ponderado a partir da matriz de adjacência
G = nx.Graph(adjacency_matrix)
# Configurações de plotagem
pos = nx.spring_layout(G) # Layout para organizar os nós
# Plotar o grafo
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
plt.title('Grafo Não Ponderado Representado por Matriz de Adjacência')
plt.show()