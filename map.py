import folium; f_map = folium.Map; f_circle = folium.CircleMarker
import osmapi; osm_nodesget = osmapi.OsmApi().NodesGet; osm_nodeways = osmapi.OsmApi().NodeWays
import pickle # deserialize list from file
import json
import tqdm; tqdm = tqdm.tqdm # progress bar

tileset = r'https://api.mapbox.com/styles/v1/mapbox/streets-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamRpZWdvZ29uemFsZXMiLCJhIjoiY2l3aHV5MmhvMDAwNzJ0cGVrdmt5MDBxNSJ9.-4RsCL1bSGLP2A_x9XFNbQ'
map = f_map(location=[-12.0786,-77.0551], tiles=tileset, attr="Grafiteros", zoom_start=15) # coordinates from openstreetmaps.org

with open("in/nodesIds.p", "rb") as bfile:
    nodesIds = pickle.load(bfile)

_half = len(nodesIds)/2
nodesIds1 = nodesIds[:_half]
nodesIds2 = nodesIds[_half:]

_raw_nodes = osm_nodesget(nodesIds1).values() + osm_nodesget(nodesIds2).values()


intersection_nodes = []
for node in tqdm(_raw_nodes):
    if "lat" in node.keys():
        cd = [node["lat"], node["lon"]]
        n = {'id': node["id"], 'coordinates': cd}
        f_circle(cd, radius=10).add_to(map)
        intersection_nodes.append(n)

map.save("map.html")

with open("in/nodes.p", "wb") as bfile:
    pickle.dump(intersection_nodes, bfile)
