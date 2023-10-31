import googlemaps
from pprint import pprint

gmaps = googlemaps.Client(key=input("Your Google API Key: "))

places_result = gmaps.places(query=input('Enter a search word: '), location=input('Enter a location: '))

place_ids = []
for place in places_result['results']:
    place_ids.append(place['place_id'])
leads = {}
ct = 1
for place_id in place_ids:
    place_details = gmaps.place(place_id=place_id)
    leads[ct] = {}
    leads[ct]['name'] = place_details['result']['name']
    if 'formatted_phone_number' in place_details['result']:
        leads[ct]['formatted_phone_number'] = place_details['result']['formatted_phone_number']
    if 'website' in place_details['result']:
        leads[ct]['website'] = place_details['result']['website']
    ct += 1
pprint(leads)

