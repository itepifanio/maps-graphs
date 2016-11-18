import requests
import json

pre = "http://nominatim.openstreetmap.org/search?format=json&limit=1&q="
address = str(raw_input("Enter an address: "))
url = pre + address

query = requests.get(url).json()
lat = query[0]["lat"]
lon = query[0]["lon"]

print "\nCoordinates: " + lat + ", " + lon + "\n"
print json.dumps(query, indent = 2)
