import requests
import json

pre = "http://nominatim.openstreetmap.org/reverse?format=json&addressdetails=1&lon="
lon = input("Enter longitude: ")
lat = input("Enter latitude: ")
post = "&lat="

url = pre + str(lon) + post + str(lat)

query = requests.get(url).json()
address = query["display_name"]
city = query["address"]["city"]

print "\nAddress: " + address
print "City: " + city + "\n"
print json.dumps(query, indent = 2)
