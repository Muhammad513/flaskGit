import requests
country=input()
url=f"https://restcountries.eu/rest/v2/name/{country}"
data=requests.get(url).json()
data=data[0]['borders']
for items in data:
    url_1=f"https://restcountries.eu/rest/v2/name/{items}"
    dt=requests.get(url_1).json()
    print(dt[0]['name'])