import matplotlib.pyplot as plt
import networkx as nx

def plotar_arvore_genealogica():
    G = nx.DiGraph()


    #Adicionando nós
    G.add_node("André")
    G.add_node("Nilza")
    G.add_node("Adilson")
    G.add_node("Rita")
    G.add_node("Auro")
    G.add_node("Ivone")
    G.add_node("Wilson")

    #Adicionando Arestas
    G.add_edge("Rita", "Nilza")
    G.add_edge("Auro", "Nilza")
    G.add_edge("Ivone", "Adilson")
    G.add_edge("Wilson", "Adilson")
    G.add_edge("Nilza", "André")
    G.add_edge("Adilson", "André")

    #Plotando
    pos = nx.spring_layout(G)
    nx.draw(G, pos,with_labels=True,node_size=3000,node_color='skyblue',font_size=10,font_weight='bold')
    plt.show()

plotar_arvore_genealogica()