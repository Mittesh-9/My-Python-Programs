import requests as rs
from bs4 import BeautifulSoup

url = input("Enter Link: ")
if ("https" or "http") in url:
    data = rs.get(url)
else:
    data = rs.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Writing the output to a file (Links.txt) instead of tp stdout
# You can change "a" to "w" to overwrite the file each time
with open("myLinks.txt", "a") as saved:
    print(links[:10], file = saved)