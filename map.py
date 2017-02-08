import folium; f_map = folium.Map; f_circle = folium.CircleMarker
import osmapi; osm_nodesget = osmapi.OsmApi().NodesGet
import pickle # deserialize list from file

tileset = r'https://api.mapbox.com/styles/v1/mapbox/streets-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamRpZWdvZ29uemFsZXMiLCJhIjoiY2l3aHV5MmhvMDAwNzJ0cGVrdmt5MDBxNSJ9.-4RsCL1bSGLP2A_x9XFNbQ'
get_map = f_map(location=[-12.0786,-77.0551], tiles=tileset, attr="Grafiteros", zoom_start=15) # coordinates from openstreetmaps.org

with open("nodes.p", "rb") as bfile:
    nodes = pickle.load(bfile)

_half = len(nodes)/2
nodes1 = nodes[:_half]
nodes2 = nodes[_half:]

nodes = osm_nodesget(nodes1).values() + osm_nodesget(nodes2).values()

coordinates = []

for x in nodes:
    if "lat" in x.keys():
        coordinates.append([x["lat"], x["lon"]])


[f_circle(xy, radius=10).add_to(get_map) for xy in coordinates]

get_map.save("index.html")

# serialization in binary
with open("coordinates.p", "wb") as bfile:
    pickle.dump(coordinates, bfile)
