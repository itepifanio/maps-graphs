import json
from waysInMap import waysInBoundingBox

ways = waysInBoundingBox(-77.0530, -12.1088, -77.0458, -12.0987)
nodesPerWay = []

def intersections():
    for result in ways:
        nodeIds = result['data']['nd']
        tags = result['data']['tag']

        if 'name' in tags.keys():
            #print json.dumps(result, indent=2, default=str)
            nodesPerWay.append({
                'streetName': tags['name'],
                'intersections': nodeIds
            })

    return nodesPerWay

# print json.dumps(nodesPerWay, indent=2, default=str)
