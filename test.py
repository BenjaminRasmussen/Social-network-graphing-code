import io
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from matplotlib import pylab


def main():
    render()


def render():
    def read():
        _lines = []
        for lines in open("data_01"):
            _lines.append(str(lines).rstrip('\n'))
        return _lines[2:]

    def encodeDict():
        # !! (str(i).split(' '))[0] gets the first item on a line in _line
        temp = defaultdict(list)
        _list = read()
        # Initialize empty lists for every user
        for i in _list:
            temp[(str(i).split(' '))[0]] = []

        for j in range(1, len(_list)):
            temp[(str(_list[j]).split(' ')[0])].append(str(_list[j]).split(' ')[1])
        return temp

    def twolists():
        ListA = []
        ListB = []
        temp = encodeDict()
        for i in range(1, 334):
            ListA.append(str(i))
            ListB.append(temp[str(i)])
        return (ListA, ListB)

    def drawgraph():
        data = twolists()
        lista, listb, = data[0], data[1]
        edges = []
        for i in range(len(data[0])):
            for j in listb[i]:
                _tuple = (lista[i], j)
                edges.append(_tuple)
        G = nx.Graph()
        G.add_nodes_from(data[0])
        G.add_edges_from(edges, alpha="0.2")

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

    drawgraph()


if __name__ == "__main__":
    main()



