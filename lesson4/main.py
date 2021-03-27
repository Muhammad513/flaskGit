import requests
import json
date="2015-02-25"
url=f'https://api.exchangeratesapi.io/{date}'
payloads={
    "base":"USD",
    "symbols":["EUR","GBP","CAD","TRY",]}
r=requests.get(url,params=payloads).json()

