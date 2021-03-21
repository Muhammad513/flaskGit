import requests
import json
data=requests.get('https://randomuser.me/api/?gender=male&results=10')
data1=data.json()
for item in data1['results'][0:10]:
    str1=str(item)
    with open("str_2.txt","a",encoding="UTF-8") as text:
        text.write(str1+'\n')