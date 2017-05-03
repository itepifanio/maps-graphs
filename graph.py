import pickle
import networkx as networkx
import networkx as nx
import matplotlib.pyplot as plt
from geopy.distance import vincenty
import tqdm; tqdm = tqdm.tqdm # progress bar
import csv



with open("in/nodes.p", "rb") as bfile:
    nodes = pickle.load(bfile)

nodesIds = []
coordinates = []
for node in nodes:
    nodesIds.append(node["id"])
    coordinates.append([node["coordinates"][0], node["coordinates"][1]]) #lat, lon

# Read Comercios_Lima.csv
comercios = []
with open('in/Comercios_Lima.csv', 'rb') as csvfile:
    comercios_csv = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in comercios_csv: # import every row as a tuple (lat, lon)
        comercios.append(tuple(row))

for node in nodes: # add a 'data' field to every node dict
    node['data'] = []

for coord1 in tqdm(comercios):
    distances = [] # store the distance of each given coordinate to a single node
    for node in nodes:
        coord2 = (node["coordinates"][0], node["coordinates"][1])
        distance = vincenty(coord1, coord2).meters
        if distance < 1000:
            distances.append({ 'nd': node["id"], 'd': distance, 'xy': coord1})
    if distances:
        distances.sort(key=lambda x:x['d']) # sort the stored distances to retrieve a smallest one
        for node in nodes: # attach the coord associated to the shortest distance to the
            if node['id'] == distances[0]['nd']:
                node['data'].append(distances[0]['xy'])

print len(nodes)
print len(coordinates)

print nodes

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
    positions[nodeId] = [xy[1],xy[0]]
    G.node[nodeId]["coordinates"] = { "lat": xy[0], "lon": xy[1]}



nx.draw_networkx_nodes(G, pos=positions, node_size=1, node_color="k")

plt.savefig("out/graph.png")

nx.draw_networkx(G, with_labels=False, pos=positions, node_size=2, node_color="b", width=0.5)
plt.savefig("out/graph-connected.png")

print nx.adjacency_matrix(G)
