import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd

# Criação de um grafo direcionado

G = nx.DiGraph()

# Adição das variáveis como nós do grafo
G.add_node("a")
G.add_node("b")
G.add_node("c")


G.add_edge("a", "b", weight=1)
G.add_edge("a", "c", weight=2)
#G.add_edge("b", "c", weight=5)

# Definição da dimensão dos nós
node_size = 2700

# Definição da cor dos nós
node_color = 'black'

# Definição da escala de cores das retas (correspondência com as correlações)
cmap = plt.colormaps.get_cmap('coolwarm_r')

# Criação de uma lista de espessuras das arestas proporcional às correlações
edge_widths = [15, 25]

# Criação do layout do grafo com maior distância entre os nós
pos = nx.spring_layout(G, k=0.75)  # k para controlar a distância entre os nós

# Desenho dos nós e das arestas com base nas correlações e espessuras
nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_color)
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=[1,3],
                       edge_cmap=cmap, alpha=0.7)

# Adição dos rótulos dos nós
labels = {"a": "labelA", "b": "labelB", "c": "labelC"}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='white')

# Ajuste dos limites dos eixos
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")

# Criação da legenda com a escala de cores definida
smp = cm.ScalarMappable(cmap=cmap)
smp.set_array([1, 4])
cbar = plt.colorbar(smp, ax=ax, label='Correlação')

# Exibição do gráfico
plt.show()
