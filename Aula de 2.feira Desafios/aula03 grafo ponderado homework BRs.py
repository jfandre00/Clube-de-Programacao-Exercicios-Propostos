import networkx as nx
import matplotlib.pyplot as plt

class Graph:
  def __init__(self):
    self.graph = nx.Graph()

  def add_edge(self, node1, node2, weight):
    self.graph.add_edge(node1, node2, weight=weight)

#Exemplo de uso
g = Graph()
g.add_edge('Brasília','Belém (PA)',1959)
g.add_edge('Brasília','Fortaleza (CE)',2038)
g.add_edge('Brasília','Maraú (BA)',1558)
g.add_edge('Brasília','Rio de Janeiro (RJ)',1179)
g.add_edge('Brasília','Santos (SP)',1105)
g.add_edge('Brasília','Bela Vista (MS)',1459)

#Plotagem do gráfico
pos = nx.spring_layout(g.graph) #layout para organizar os nós
labels = nx.get_edge_attributes(g.graph, 'weight') #obtem os pesos das arestas

nx.draw(g.graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(g.graph, pos, edge_labels=labels)
plt.title('Grafo Ponderado')
plt.show()