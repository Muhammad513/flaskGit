import requests
country=input()
url=f"https://restcountries.eu/rest/v2/name/{country}"
data= requests.get(url).json()[0]
for i in data['borders']:
    url_bor=f"https://restcountries.eu/rest/v2/name/{i}"
    r=requests.get(url_bor).json()[0]['currencies'][0]['code']
    url_1='https://free.currconv.com/api/v7/convert'
    pyload={
        'apiKey':'fc6523f34ba2aa837bc6',
        'compact':'ultra',
        'q':f'{r}_UZS'
    }
    dta=requests.get(url_1,params=pyload).json()
    print(dta)
    
    

