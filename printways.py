import osmapi

import pprint




def WaysInMap(w,x,y,z):
    api = osmapi.OsmApi()

    BBox = api.Map(w,x,y,z)


    calles = list()
    for i in BBox:
        if i[u'type'] == u'way':
            calles.append(i)

    return calles





