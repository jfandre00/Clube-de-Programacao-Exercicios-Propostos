#Exemplo 3

import networkx as nx
import matplotlib.pyplot as plt

# Criar o grafo
G = nx.Graph()

# Adicionar os nós
G.add_nodes_from([1, 2, 3, 4, 5, 6])

# Adicionar as arestas
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (2, 4), (4, 6)])

# Identificar o ciclo
cycle = nx.find_cycle(G)

# Criar uma lista de arestas do ciclo
cycle_edges = [(cycle[i][0], cycle[i][1]) for i in range(len(cycle))]

# Criar uma lista de arestas que não pertencem ao ciclo
non_cycle_edges = [edge for edge in G.edges() if edge not in cycle_edges]

# Definir as cores das arestas


edge_colors = ['r' if edge in cycle_edges else 'b' for edge in G.edges()]

# Desenhar o grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edgelist=non_cycle_edges, edge_color='b')
nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color='r')
nx.draw_networkx_labels(G, pos)
plt.show()