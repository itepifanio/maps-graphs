import pickle
import networkx as networkx
import networkx as nx
import matplotlib.pyplot as plt

with open("in/nodes.p", "rb") as bfile:
    nodes = pickle.load(bfile)

nodesIds = []
coordinates = []
for node in nodes:
    nodesIds.append(node["id"])
    coordinates.append([node["coordinates"][0], node["coordinates"][1]]) #lat, lon

print len(nodes)
print len(coordinates)

with open("in/edges.p", "rb") as bfile:
    edges = pickle.load(bfile)

print len(edges)
for time in [1,2,3]:
    for edge in edges:
        for x in edge:
            if x not in nodesIds:
                edges.remove(edge)
print len(edges)

check = []
for edge in edges:
    for x in edge:
        check.append(x)

print len(set(check))

G=nx.Graph()
G.add_nodes_from(nodesIds)
G.add_edges_from(edges)

positions = {}
for nodeId, xy in zip(nodesIds, coordinates): #pythonic way of iterating over two lists
    positions[nodeId] = [xy[0],xy[1]]

try:
    nx.draw_networkx_nodes(G, pos=positions, node_size=1, node_color="k")
except networkx.exception.NetworkXError:
    pass;

plt.savefig("out/graph.png")

nx.draw_networkx(G, with_labels=False, pos=positions, node_size=2, node_color="b", width=0.5)
plt.savefig("out/graph-connected.png")

print nx.adjacency_matrix(G)
