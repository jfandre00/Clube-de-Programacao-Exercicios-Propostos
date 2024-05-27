import networkx as nx
import matplotlib.pyplot as plt

#Criando um grafo simples
G = nx.Graph()

#Adicionando um laço no vértice A
G.add_edge('A','A')

#Plotando o gráfico
pos = nx.circular_layout(G) #Define a posição dos nós em um círculo
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')

plt.show()