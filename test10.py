import networkx as nx
import matplotlib.pylab as plt
import scipy.stats as sp
import numpy as np

G = nx.degree(G=nx.read_adjlist("WH"))
options = {
    'node_color': 'black',
    'edge_color': 'blue',
    'node_size': 5,
    'alpha': 0.2,
    'width': 1,
    'node_shape': 'X',
}
temp = []
for i in list(G):
    try:
        temp.append(float(i[1]))
    except:
        pass
temp.sort()
h = enumerate(range(0,len(temp)))
_temp = []
for i in temp:
    if i > 15:
        _temp.append(i)


_temp = np.array(_temp)
d = np.diff(np.unique(_temp)).min()
left_of_first_bin = _temp.min() - float(d)/2
right_of_last_bin = _temp.max() + float(d)/2
plt.hist(_temp,np.arange(left_of_first_bin, right_of_last_bin + d, d))
plt.xscale("log")
plt.yscale("log")
plt.xlabel("x amount of followers, log scale")
plt.ylabel("y is amount of users with x followers count, log scale")
plt.title("Histogram for degree distribution of Twitter users")
plt.savefig("Twitter Histogram log.png", dpi=500)

plt.show()
