import requests
token = "cf6c4488d9de440389453aa6fa61f69f"
headers={
    "X-Api-Key":token
}
country=input()
number=int(input())
pyloads={
    'CountryCode':country,
    'Quantity':number
}

url='https://randommer.io/api/Phone/Generate'
data=requests.get(url,params=pyloads,headers=headers).json()
for i in data:
    print(i)
