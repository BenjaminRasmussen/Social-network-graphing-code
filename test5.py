import networkx as nx

import mmap

with open("links-anon.txt", "r+") as f:
    # memory-map the file, size 0 means whole file
    map = mmap.mmap(f.fileno(), 10 ** 9)
    # read content via standard file methods
    while map.readline():
        print(str(map.readline())[2:-3].split(' ')[1])
        nx.generate_adjlist(nx.Graph.add_edges_from(str(map.readline())[2:-3].split(' ')[0],
                                              str(map.readline())[2:-3].split(' ')[1]))
        # prints "Hello Python!"
    # read content via slice notation
    # update content using slice notation;
    # note that new content must have same size
    # ... and read again using standard file methods

    # close the map
    map.close()
