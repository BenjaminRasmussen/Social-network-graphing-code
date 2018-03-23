import networkx as nx

nx.write_adjlist(nx.read_edgelist(open("links-anon.txt", "rb", buffering=1).readlines()), "HW")
