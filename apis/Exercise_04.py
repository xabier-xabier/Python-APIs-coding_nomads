'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 676,
    "first_name": "eoplkjh",
    "last_name": "hnsmskhh",
    "email": "polik@gmail.com"
}

# here we execute the PUT request
response = requests.put(base_url +"/676", json=body)
# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your updated record?
print(f"Response Content: {response.content}")