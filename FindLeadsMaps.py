from pprint import pprint
import time
# API_KEY = "AIzaSyB2iMF8nM3W-tC1mdayXY3yYe0EqXi2fYg"
import requests
import json

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyB2iMF8nM3W-tC1mdayXY3yYe0EqXi2fYg')
query = input("Enter a query: ")
location = input('Enter a location: ')

# Perform a text search for restaurants in a specific location
places_result = gmaps.places(query=query, location=location)

leads_ids = []
for i in places_result['results']:
     leads_ids.append(i['place_id'])

leads = {}
id = 1
for j in leads_ids:
    place_details = gmaps.place(place_id=j)
    leads[id] = {}
    leads[id]['name'] = place_details['result']['name']
    leads[id]['formatted_address'] = place_details['result']['formatted_address']
    if "formatted_phone_number" in place_details["result"]:
        leads[id]['formatted_phone_number'] = place_details['result']['formatted_phone_number']
    if "website" in place_details["result"]:
        leads[id]['website'] = place_details['result']['website']
    id += 1

pprint(leads)


