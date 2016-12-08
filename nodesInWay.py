# -*- coding: utf-8 -*-
import sys; sys.dont_write_bytecode = True # avoid .pyc files
import json, osmapi, itertools, folium

Lima = folium.Map(location=[-12.0621064, -77.0365255], zoom_start=12)
OSM = osmapi.OsmApi()

def waysInBoundingBox(w,x,y,z):
    boundingBox = OSM.Map(w,x,y,z)
    ways = []
    for result in boundingBox:
        if result['type'] == 'way':
            ways.append(result)
    return ways

def streetWithNodes(ways):
    nodes = []
    for way in ways:
        nodeIds = way['data']['nd']
        tags = way['data']['tag']

        if 'name' in tags.keys() and 'highway' in tags.keys(): # check if we are talking about a street (has name and highway within its tags)
            '''
            nodes.append({
                'streetId': way['data']['id'],
                'streetName': tags['name'],
                'nodesInStreet': nodeIds
            })
            '''
            nodes.append(nodeIds)
    return nodes

nodes = streetWithNodes(waysInBoundingBox(-77.0530, -12.1088, -77.0458, -12.0987)) # bounding box for Jesus María: http://isithackday.com/geoplanet-explorer/index.php?woeid=22723450
#-77.05806, -12.08566, -77.039459, -12.06748
# print json.dumps(streetWithNodes, indent=2, default=str)

'''
for i, val in enumerate(nodes):
    print nodes[i]['nodesInStreet']
'''

tmp = []
for x, left in enumerate(nodes):
    for y, right in enumerate(nodes):
        common = list(set(left) & set(right))
        if common:
            tmp.append(common)

tmp2 = set(list(itertools.chain.from_iterable(tmp)))

# coordinatesPerNode is a list comprised of lists with the following form:
# [
# [34.234, 23.1456],
# [32.144, 25.9726],
# ...
# ]
coordinatesPerNode = []

for i in tmp2:
    node = OSM.NodeGet(i)
    if node['tag']: # Check if dict is empty, empty dicts evaluate to False
        #print json.dumps(node, indent=2, default=str)
        coordinatesPerNode.append([node['lat'],node['lon']])

# print len(coordinatesPerNode)

# Remove duplicates, similar behavior as set() but for lists within lists
coordinates = []
for i in coordinatesPerNode:
  if i not in coordinates:
    coordinates.append(i)

print len(coordinates)

# Add markers per every [lat,lon]
for i in coordinates:
    folium.Marker(location=i).add_to(Lima)

Lima.save('index.html')
