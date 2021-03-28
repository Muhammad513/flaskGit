import requests
token = "cf6c4488d9de440389453aa6fa61f69f"

headers={
    "X-Api-Key":token
}

url='https://randommer.io/api/Card'

data=requests.get(url,headers=headers).json()
print(data)