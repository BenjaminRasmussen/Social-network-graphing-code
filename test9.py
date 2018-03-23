import networkx as nx
import matplotlib.pylab as plt
G = nx.read_adjlist("WH")

options = {
    'node_color': 'black',
    'edge_color': 'blue',
    'node_size': 5,
    'alpha': 0.2,
    'width': 1,
    'node_shape': 'X',
}

nx.draw_kamada_kawai(G, color="black", with_labels=False, font_weight='bold', **options)
plt.savefig("path.png", dpi=500)
plt.show()