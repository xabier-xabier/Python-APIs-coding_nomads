'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
# Compare Spain and Indonesia

import requests
from pprint import pprint


def population(num1,num2):
    if num1>num2:
        dif=num1-num2

    else:
        dif=num2-num1

    return dif



url="https://restcountries.com/"

# info for Spain population
response_lan=requests.get("https://restcountries.com/v3.1/name/spain")

resp_lan=response_lan.json()
pop_spain=resp_lan[0]["population"]

#info for Indonesia population

response_indo=requests.get("https://restcountries.com/v3.1/name/indonesia")
resp_indo=response_indo.json()

pop_indo=resp_indo[0]["population"]

dif_pop=population(pop_indo,pop_spain)

if pop_indo > pop_spain:
    print(f"Indonesia is bigger in: {dif_pop}")

else:
    print(f"Spain is bigger in: {dif_pop}")

print(f"The total population of Spain is: {pop_spain}")
print(f"The total population of Indonesia is: {pop_indo}")

#pprint((response_lan.text))

# Print the names of each countries and their capitals
print("--------------------------------------------------")
print(resp_indo[0]["name"]["official"])
print(resp_lan[0]["name"]["official"])
print("--------------------------------------------------")
print("the capital of Indonesia is: ",resp_indo[0]["capital"])
print("the capital of Spain is: ",resp_lan[0]["capital"])
print("--------------------------------------------------")

# Area difference


area_spain=resp_lan[0]["area"]
area_indo=resp_indo[0]["area"]

res=population(area_indo,area_spain)

if area_indo>area_spain:
    print("Indonesia`s land is bigger")
    print(f"the difference is : {res}")

else:
    print("Spain`s land is bigger")
    print(f"the difference is : {res} km2")

