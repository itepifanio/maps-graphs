__author__ = "Carlos Fabbri"
import osmapi
import pprint
from printways import WaysInMap

api = osmapi.OsmApi()

print("verificamos que se inicializo... \n")
print(api.NodeGet(123), "\n")

#bounding box de un sector de la molina
BBox = api.Map(-76.89914, -12.08569, -76.89676, -12.08411)

#compuesto por nodes y ways
print(BBox)
print(len(BBox))

#probemos con uno de los elementos...
una_calle = BBox[-1]

print(type(una_calle))

print(una_calle.keys())
#su primera division es en data y en type

data_de_calle = una_calle[u'data']

print(type(data_de_calle))
#sigue siendo diccionario

pprint.pprint(data_de_calle)

print(data_de_calle[u'nd'])
#hemos conseguido extraer los nodos de una calle



