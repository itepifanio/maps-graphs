import sys; sys.dont_write_bytecode = True # avoid .pyc files
import json
from waysInMap import waysInBoundingBox

ways = waysInBoundingBox(-77.0530, -12.1088, -77.0458, -12.0987)
nodesPerStreet = []

for result in ways:
    nodeIds = result['data']['nd']
    tags = result['data']['tag']

    if 'name' and 'highway' in tags.keys(): # check if we are talking about a street (has name and highway within its tags)
        nodesPerStreet.append({
            'streetId': tags['name'].
            'streetName': tags['name'],
            'nodesInStreet': nodeIds
        })

print json.dumps(nodesPerStreet, indent=2, default=str)

# print json.dumps(nodesPerWay, indent=2, default=str)
