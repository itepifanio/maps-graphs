import osmapi; osmapi = osmapi.OsmApi(); osm_nodesget = osmapi.NodesGet; osm_nodeways = osmapi.NodeWays
import pickle # deserialize list from file
import tqdm; tqdm = tqdm.tqdm # progress bar
import json

# first, let's open the list of node IDs
with open("in/ways.p", "rb") as bfile:
    ways = pickle.load(bfile)

# first, let's open the list of node IDs
with open("in/nodes.p", "rb") as bfile:
    nodes = pickle.load(bfile)

nodesIds = []
for node in nodes:
    nodesIds.append(node["id"])

print len(nodesIds)

for way in tqdm(ways):
    for nodeId in way["data"]["nd"]:
        try:
            nodesIds.index(nodeId)
        except ValueError:
            way["data"]["nd"].remove(nodeId)

check = []
edges = []
for way in tqdm(ways):
    for index, nodeId in enumerate(way["data"]["nd"]):
        if nodeId in nodesIds:
            check.append(nodeId)
            try:
                edge = (nodeId,way["data"]["nd"][index+1])
                edges.append(edge)
            except IndexError:
                pass;
        else:
            way["data"]["nd"].remove(nodeId)

print len(set(check))
print edges

# first, let's open the list of node IDs
with open("in/edges.p", "wb") as bfile:
    pickle.dump(edges, bfile)
