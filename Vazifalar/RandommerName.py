import requests
token = "cf6c4488d9de440389453aa6fa61f69f"
headers={
    "X-Api-Key":token
}
number=int(input())
payloads={
    "nameType" : "fullname",
    "quantity" : number
}

url=f'https://randommer.io/api/Name'

data=requests.get(url,params=payloads,headers=headers).json()
for items in data:
    print(items)