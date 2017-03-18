import osmapi; osmapi = osmapi.OsmApi(); osm_nodesget = osmapi.NodesGet; osm_nodeways = osmapi.NodeWays
import pickle # deserialize list from file
import tqdm; tqdm = tqdm.tqdm # progress bar

with open("nodes.p", "rb") as bfile:
    nodes = pickle.load(bfile)

relations = {}

for node in tqdm(nodes):
    node_relations = osmapi.NodeRelations(node)
    relations[node] = node_relations

print json.dumps(relations, indent=2, default=str)
