'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and post on the forum ;)

'''
import requests
from pprint import pprint

url_chuck="https://api.chucknorris.io/jokes/random"

respo_chuck=requests.get(url_chuck)

resp=respo_chuck.json()
pprint((type(resp["value"])))

spl=resp["value"].split()

print(spl)
print(spl[-1])


resp_word=requests.get("https://api.datamuse.com/words?rel_rhy="+spl[-1])
url="https://api.datamuse.com/words?rel_rhy="+spl[-1]                           # sometimes doesn`t work, loses the link to the web page`
resp_word=requests.get("https://api.datamuse.com/words?rel_rhy=existence")   # If a set the link to any word works but  '+spl[-1]' not catching well

resp_w=resp_word.json()

change=resp_w[0]["word"]

spl[-1]=change

string=""
for i in spl:
    string+=i+" "
    
print(string)


