import folium; f_map = folium.Map; f_circle = folium.CircleMarker
import osmapi; osm_nodeget = osmapi.OsmApi().NodeGet
import pickle # deserialize list from file

get_map = f_map([-12.0786,-77.0551], zoom_start=16) # coordinates from openstreetmaps.org

with open("nodes.p", "rb") as bfile:
    nodes = pickle.load(bfile)

def getCoordinates(x):
    x = osm_nodeget(x)
    return [x["lat"], x["lon"]]

coordinates = map(getCoordinates, nodes)

[f_circle(xy, radius=10).add_to(get_map) for xy in coordinates]

get_map.save("index.html")
