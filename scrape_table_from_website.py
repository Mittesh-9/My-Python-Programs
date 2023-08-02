import urllib.request
import pandas as pd

url = "https://trends.builtwith.com/websitelist/DataTables"

with urllib.request.urlopen(url) as i:
    html = i.read()

data = pd.read_html(html)[0]
print(data.head())