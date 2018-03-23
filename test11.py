import networkx as nx
import matplotlib.pylab as plt
import scipy.stats as stats
import numpy as np

G = nx.degree(G=nx.read_edgelist("carolinedata"))
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
# temp.sort()
h = enumerate(range(0, len(temp)))

print(temp)
x1 = np.array(temp)  # random data, normal distribution
xs = np.linspace(x1.min() - 1, x1.max() + 1, len(x1))
print(x1)

kde1 = stats.gaussian_kde(x1)
kde2 = stats.gaussian_kde(x1, bw_method='silverman')

fig = plt.figure(figsize=(8, 6))

plt.plot(xs, kde2(xs), 'b-', label="Happiness line")
plt.legend(loc=1)
plt.xlabel("Exercise hours per week")
plt.ylabel("happiness density distribution")
plt.title("Probability density function for exercise versus happiness ")
plt.savefig("m silverman log non ranged estimation.png", dpi=500)
plt.show()
