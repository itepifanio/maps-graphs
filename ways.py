import sys; sys.dont_write_bytecode = True # avoid .pyc files
import json
import osmapi; osmapi = osmapi.OsmApi(); osm_map = osmapi.Map; osm_nodeways = osmapi.NodeWays; osm_nodeget
import folium
from tqdm import tqdm # progress bar

# array of objects (list of dict), bounding box for Jesus Maria, Lima, Peru
bbox = osm_map(-77.063135, -12.093128, -77.039006, -12.064528) # coordinates via boundingbox.klokantech.com
nds = []
nds_append = nds.append

def filterWays(x):
    # check if we are talking about a street (has name and highway within its tags)
    if x['type'] == 'way' and 'name' in x['data']['tag'].keys() and 'highway' in x['data']['tag'].keys():
        # check if we is not a litle pathway i.e. in the middle of a park
        # if x['data']['tag']['highway'] is not ("footway" or "cycleway" or "path" or "service" or "track"):
            return True

ways = filter(filterWays, bbox)

def filterWays2(x):
    if 'name' in x['tag'].keys() and 'highway' in x['tag'].keys():
        # if x['tag']['highway'] is not ("footway" or "cycleway" or "path" or "service" or "track"):
            return True

for way in tqdm(ways):
    id1 = way['data']['id']
    nodeIds = way['data']['nd']
    for nd in nodeIds:
        ways2 = filter(filterWays2, osm_nodeways(nd))
        for way in ways2:
            id2 = way['id']
            if id1 != id2: # for some reason `is not` does not behave as `!=`
                nds_append(nd)

# remove duplicates
nds = list(set(nds))

#print json.dumps(ways, indent=2, default=str)
#print nds
print len(nds)
'''
nodeIds = result['data']['nd']
#if result['data']['tag']['highway'] is not ("footway" or "cycleway" or "path" or "service" or "track"):
ways.append({
    'streetId': result['data']['id'],
    'streetName': tag['name'],
    'nodesInStreet': nodeIds
})
'''
