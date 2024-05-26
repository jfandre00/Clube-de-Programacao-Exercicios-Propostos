import networkx as nx
import matplotlib.pyplot as plt

#Plote o grafo G=(V,E) dado V={1,2,3} e E={(1,2),(1,3),(2,3)}.

#Cria um grafo não direcionado
G = nx.Graph()

#Adiciona nós ao grafo
G.add_nodes_from([1, 2, 3])

#Adiciona arestas ao grafo
G.add_edges_from([(1,2), (1,3), (2,3)])

#Visualiza o grafo
nx.draw(G, with_labels=True, node_color='lightblue', node_size=800, font_size=12, font_weight='bold')
plt.title("Grafo com Nós e Arestas")
plt.show()