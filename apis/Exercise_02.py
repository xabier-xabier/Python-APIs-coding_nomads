'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

data = response.json()
data1=data["data"]
#pprint(data1)
#pprint(type(data["data"][0]))

list=[]
for i in data1:
    list.append(i["email"])

for j in list:
    print(j)
