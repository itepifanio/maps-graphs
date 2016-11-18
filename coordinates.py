import requests
import json

pre = "http://nominatim.openstreetmap.org/reverse?format=json&addressdetails=1&lat="
lat = input("Enter latitude: ")
lon = input("Enter longitude: ")
post = "&lot="

url = pre + str(lat) + post + str(lon)

query = requests.get(url).json()
address = query["display_name"]
city = query["address"]["city"]

print "\nAddress: " + address
print "City: " + city + "\n"
print json.dumps(query, indent = 2)
