__author__ = "Carlos Fabbri"
import osmapi
import pprint
from printways import WaysInMap

api = osmapi.OsmApi()


calles = WaysInMap(-77.0530, -12.1088, -77.0458, -12.0987)

for i in calles:
    calle_con_nodos = list()
    datos = i[u'data']
    datos2 = datos[u'tag']
    if u'name' in datos2.keys():
        calle_con_nodos.append(datos2[u'name'])

    calle_con_nodos.append(datos[u'nd'])
    print(calle_con_nodos)








