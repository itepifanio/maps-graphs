import pickle
import networkx as nx
import matplotlib.pyplot as plt

with open("coordinates.p", "rb") as bfile:
    coordinates = pickle.load(bfile)

G=nx.Graph()
G.add_nodes_from(range(len(coordinates)))

edges = []
for x in range(len(coordinates)-1):
    edges.append((x,x+1))

G.add_edges_from(edges)

positions = {}
for index, xy in enumerate(coordinates):
    positions[index] = [xy[0],xy[1]]

nx.draw_networkx_nodes(G, pos=positions, node_size=1, node_color="k")
plt.savefig("graph.png")

nx.draw_networkx(G, with_labels=False, pos=positions, node_size=1, node_color="k", width=0.1)
plt.savefig("graph-connected.png")

print nx.adjacency_matrix(G)
