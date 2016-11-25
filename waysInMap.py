import sys; sys.dont_write_bytecode = True # avoid .pyc files
import osmapi
import json

OSM = osmapi.OsmApi()

def waysInBoundingBox(w,x,y,z):
    boundingBox = OSM.Map(w,x,y,z)
    ways = []
    for result in boundingBox:
        if result['type'] == 'way':
            ways.append(result)
    return ways
    # print json.dumps(ways, indent=2, default=str)
