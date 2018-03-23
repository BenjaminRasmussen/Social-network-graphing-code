import networkx as nx

allhigh = 38821855949
curhigh = allhigh
curlow = 0
with open("links-anon.txt") as fin:
    fin.seek(0)
    data = fin.read(int(38821855948/1000000) - 0)
    l = []
    for i in "\n".join(data.split('\n')[1:-1]).split("\n"):
        l.append((str(i).split(' ')[0],str(i).split(' ')[1]))

    options = {
        'node_color': 'black',
        'edge_color': 'blue',
        'node_size': 5,
        'alpha': 0.2,
        'width': 1,
        'node_shape': 'X',

    }
    fh = open("wq", "wb")
    G = nx.Graph()
    G.add_edges_from(l)
    nx.write_adjlist(G, fh)
