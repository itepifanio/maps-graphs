import sys; sys.dont_write_bytecode = True # avoid .pyc files
import json
import osmapi; osmapi = osmapi.OsmApi()
import folium
from tqdm import tqdm

# array of objects (list of dict), bounding box for Jesus Maria, Lima, Peru
bbox = osmapi.Map(-77.063135, -12.093128, -77.039006, -12.064528)

# array of objects (list of dict), containing filtered ways, actual streets and avenues
ways = []
nds = []

for result in bbox:
    tag = result['data']['tag']
    # check if we are talking about a street (has name and highway within its tags)
    if result['type'] == 'way' and 'name' in tag.keys() and 'highway' in tag.keys():
        ways.append(result)
        '''
        nodeIds = result['data']['nd']
        #if result['data']['tag']['highway'] is not ("footway" or "cycleway" or "path" or "service" or "track"):
        ways.append({
            'streetId': result['data']['id'],
            'streetName': tag['name'],
            'nodesInStreet': nodeIds
        })
        '''

for way in tqdm(ways):
    id1 = way['data']['id']
    nodeIds = way['data']['nd']
    for nd in nodeIds:
        waysOfnode = osmapi.NodeWays(nd)
        for result in waysOfnode:
            tag = result['tag']
            waysOfnode.remove(result)
            if 'name' in tag.keys() and 'highway' in tag.keys():
                waysOfnode.append(result)
        for way in waysOfnode:
            id2 = way['id']
            if id2 != id1:
                # print str(id1) + " <> " + str(id2)
                # print "########"
                # print " "
                nds.append(nd)

# remove duplicates
nds = list(set(nds))

#print json.dumps(ways, indent=2, default=str)
print(nds)
print(len(nds))
