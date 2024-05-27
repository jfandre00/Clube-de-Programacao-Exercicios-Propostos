import networkx as nx
import matplotlib.pyplot as plt

class Graph:
  def __init__(self):
    self.graph = nx.Graph()

  def add_edge(self, node1, node2, weight):
    self.graph.add_edge(node1, node2, weight=weight)

#Exemplo de uso
g = Graph()
g.add_edge('A','B',5)
g.add_edge('B','C',7)
g.add_edge('A','C',3)

#Plotagem do gráfico
pos = nx.spring_layout(g.graph) #layout para organizar os nós
labels = nx.get_edge_attributes(g.graph, 'weight') #obtem os pesos das arestas

nx.draw(g.graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(g.graph, pos, edge_labels=labels)
plt.title('Grafo Ponderado')
plt.show()