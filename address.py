import requests
import json

pre = "http://nominatim.openstreetmap.org/search?format=json&limit=1&q="
address = str(raw_input("Enter an address: "))
url = pre + address

query = requests.get(url).json()
lon = query[0]["lon"]
lat = query[0]["lat"]

print "\nCoordinates: " + lon + ", " + lat + "\n"
print json.dumps(query, indent = 2)
