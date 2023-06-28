'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import requests
import json,time
from flask import *


aap=Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
    data_set={'page':'Home','Message':'You have many task to do','Timestamp':time.time()}
    json_dump=json.dumps(data_set)

    return json_dump



@app.route('/user/', methods=['GET'])
def request_page():
    user_query=str(request.args.get('user'))  #/user/?user=USER_NAME
    data_set={'Page':'Home', 'Message':f'Request to user {user_query}','Timestamp':time.time()}
    json_dump=json.dumps(data_set)

    return json_dump

if __name__=='__main__':
    app.run(port=777)

#text=input("""Please select from the following options (enter the number of the action you'd like to take):
#1) Create a new account (POST)
#2) View all your tasks (GET)
#3) View your completed tasks (GET)
#4) View only your incomplete tasks (GET)
#5) Create a new task (POST)
#6) Update an existing task (PATCH/PUT)
#7) Delete a task (DELETE)""")

