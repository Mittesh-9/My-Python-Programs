# Needs Improvement

import geopy
from geopy.location import get_ip
from geopy.geocoders import Nominatim

ip = get_ip()
print(ip)

# geolocator = geopy.geocoders.Nominatim(user_agent="my-application")

country = geopy.country(ip)
print(country)

geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode("my location")
print(location.address)
print((location.latitude, location.longitude))
# location = geopy.geocoders.Geocoder.geocode(ip)
# print(country)


ptrData = geopy.dns.reverse_dns(ip)
print(ptrData)

geopy.showIpDetails("103.135.202.25")

geopy.showCountryDetails("103.135.202.25")