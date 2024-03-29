import requests

# Base URL for geocoding
url = "https://us1.locationiq.com/v1/search.php"

address = input("Input the address: ")

# Your unique private_token should replace value of the private token variable.

private_token = "Your private token"

data = {
    "key" : private_token,
    "q" : address,
    "format" : "json"
}

response = requests.get(url, params = data)

latitude = response.json()[0]["lat"]
longitude = response.json()[0]["lon"]

print(f"The latitude of the given address is: {latitude}")
print(f"The longitude of the given address is: {longitude}")