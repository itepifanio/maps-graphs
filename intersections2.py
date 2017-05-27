import sys; sys.dont_write_bytecode = True # avoid .pyc files
import json
import osmapi; osmapi = osmapi.OsmApi(); osm_map = osmapi.Map; osm_nodeways = osmapi.NodeWays
import folium
import tqdm; tqdm = tqdm.tqdm # progress bar
import pickle # serialize list to file for later use
from collections import Counter

# array of objects (list of dict), bounding box for Jesus Maria, Lima, Peru
bbox = osm_map(-71.564681,-16.432833,-71.513342,-16.375271)

# array of nodes representing road intersections
intersections = list()

# function to filter results coming from bbox into actual ways
def filter_ways1(x):
    # check if we are talking about a street (has name and highway within its tags)
    if x["type"] == "way" and "name" in x["data"]["tag"].keys() and "highway" in x["data"]["tag"].keys():
        # check if we is not a litle pathway i.e. in the middle of a park
        if x["data"]["tag"]["highway"] is not ("footway" or "cycleway" or "path" or "service" or "track"):
            return True

ways1 = filter(filter_ways1, bbox)
print "------------------pobando--------------------------------"
#print ways1
print "*********************"

# serialization in binary
with open("in/ways.p", "wb") as bfile:
    pickle.dump(ways1, bfile)

# function to filter results coming from osm_nodeways into actual ways
def filter_ways2(x):
    if "name" in x["tag"].keys() and "highway" in x["tag"].keys():
        if x["tag"]["highway"] is not ("footway" or "cycleway" or "path" or "service" or "track"):
            return True

###versionOriginal -D
# 3 nested for-loops:
## first, we loop through the ways of a particular area (ways1); saving their `id` and the `nodes` they hold
## then, we loop through these held `nodes` and for each of them we query their the ways they are part of; we filter this ways so that we only get actual ones (ways2)
## finally, we loop through each of these ways2 and search for the ones which differ from the initial way -- up in the initial loop -- because this would mean that the `node` in the second loop is part of more than 1 actual `way`
# for way in tqdm(ways1): # just a wrapper to get a progress bar
#     id1 = way["data"]["id"]
#     nodes = way["data"]["nd"]
#     for node in nodes:
#         ways2 = filter(filter_ways2, osm_nodeways(node))
#         for way in ways2:
#             id2 = way["id"]
#             if id1 != id2:
#                 intersections.append(node)
#
# # remove duplicates
# intersections = list(set(intersections))

######contribucion de Kinley#########################
waysNodesCollection2 = []
for way in tqdm(ways1):
    wayNodes2 = way["data"]["nd"]
    waysNodesCollection2 = waysNodesCollection2 + wayNodes2
print "XXXXXXX**********"
print "XXXXXXX**********XXXXXXXXXXX---NodosCantidadTotal"
print len(waysNodesCollection2)

#Creating a list which contains only the nodes repeated --> if they repeated, then they are intersections
intersections = [k for k,v in Counter(waysNodesCollection2).items() if v>1]

print "--------"
print "XXXXXXX**********555555555555555NodosCantidadQueSonIntersecciones"
# print intersections
# print length for cross-checking with _overpass.py
print len(intersections)
print "XXXXXXX**********FINALFINAL"
# serialization in binary
with open("in/nodesIds.p", "wb") as bfile:
    pickle.dump(intersections, bfile)
