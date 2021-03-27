import requests
usd=float(input())
val=input()
payload={
    "base":val,
    "symbols":["EUR","GBP","CAD","TRY",]
}
url="https://api.exchangeratesapi.io/latest"
r=requests.get(url,params=payload).json()
data=r['rates']
for items in data:
    print(items,data[items]*usd)
