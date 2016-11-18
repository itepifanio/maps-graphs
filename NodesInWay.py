import pprint
import json
from waysInMap import waysInBoundingBox

ways = waysInBoundingBox(-77.0530, -12.1088, -77.0458, -12.0987)
nodesPerWay = []

def intersections():
    for results in ways:
        nodeIds = results['data']['nd']
        tags = results['data']['tag']

        if 'name' in tags.keys():
            nodesPerWay.append({
                'streetName': tags['name'],
                'intersections': nodeIds
            })

    return nodesPerWay

# print json.dumps(nodesPerWay, indent=2, default=str)
