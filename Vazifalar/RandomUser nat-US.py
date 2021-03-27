import requests
number=int(input())
nat=input()
payload={
    "results":number,
    "nat":nat
}
url="https://randomuser.me/api/"
r=requests.get(url,params=payload).json()
for items in r['results']:
    with open("RandomUser.txt","a",encoding='UTF-8') as text:
         text.write(f"full name: {str(items['name']['first'])}  {str(items['name']['last'])}, city: {items['location']['city']}, email: {items['email']}, age:  {items['dob']['age']} \n")