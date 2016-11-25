import sys; sys.dont_write_bytecode = True
import osmapi
import json
from nodesInWay import intersections
import folium

OSM = osmapi.OsmApi()
intersections = intersections()

Lima = folium.Map(location=[-12.0621064, -77.0365255], zoom_start=12)

# coordinatesPerNode is a list comprised of lists with the following form:
# [
# [34.234, 23.1456],
# [32.144, 25.9726],
# ...
# ]
coordinatesPerNode = []

for entry in intersections:
    for nodeId in entry['intersections']:
        node = OSM.NodeGet(nodeId)
        if not node['tag']: # Check if dict is empty, empty dicts evaluate to False
            #print json.dumps(node, indent=2, default=str)
            coordinatesPerNode.append([node['lat'],node['lon']])

print len(coordinatesPerNode)

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
