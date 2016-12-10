import sys; sys.dont_write_bytecode = True # avoid .pyc files
import json
import osmapi; osmapi = osmapi.OsmApi(); osm_map = osmapi.Map; osm_nodeways = osmapi.NodeWays
import folium
import tqdm; tqdm = tqdm.tqdm # progress bar
import pickle # serialize list to file for later use

# array of objects (list of dict), bounding box for Jesus Maria, Lima, Peru
bbox = osm_map(-77.063135, -12.093128, -77.039006, -12.064528)

# array of nodes representing road intersections
intersections = list()

# function to filter results coming from bbox into actual ways
def filter_ways1(x):
    # check if we are talking about a street (has name and highway within its tags)
    if x["type"] == "way" and ("name" and "highway") in x["data"]["tag"].keys():
        # check if we is not a litle pathway i.e. in the middle of a park
        if x["data"]["tag"]["highway"] is not ("footway" or "cycleway" or "path" or "service" or "track"):
            return True

ways1 = filter(filter_ways1, bbox)

# function to filter results coming from osm_nodeways into actual ways
def filter_ways2(x):
    if ("name" and "highway") in x["tag"].keys():
        if x["tag"]["highway"] is not ("footway" or "cycleway" or "path" or "service" or "track"):
            return True

# 3 nested for-loops:
## first, we loop through the ways of a particular area (ways1); saving their `id` and the `nodes` they hold
## then, we loop through these held `nodes` and for each of them we query their the ways they are part of; we filter this ways so that we only get actual ones (ways2)
## finally, we loop through each of these ways2 and search for the ones which differ from the initial way -- up in the initial loop -- because this would mean that the `node` in the second loop is part of more than 1 actual `way`
for way in tqdm(ways1): # just a wrapper to get a progress bar
    id1 = way["data"]["id"]
    nodes = way["data"]["nd"]
    for node in nodes:
        ways2 = filter(filter_ways2, osm_nodeways(node))
        for way in ways2:
            id2 = way["id"]
            if id1 != id2:
                intersections.append(node)

# remove duplicates
intersections = list(set(intersections))

# print length for cross-checking with _overpass.py
print len(intersections)

# serialization in binary
with open("nodes.p", "wb") as bfile:
    pickle.dump(intersections, bfile)
