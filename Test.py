#  a script that takes in a url as an argument and carries otu basic crud

import requests
import json
import sys
from pprint import pprint



def post(url):

    body = json.dumps({
  "name": "string_test",
  "email": "blac_dev@email.com"
})
    headers = {
  'Content-Type': 'application/json'
}
    print("making post request to " + url)
    data= requests.post(url, data=body,headers=headers).text
    return data

def get(url):
    print("making get request to " + url + "/string_test")
    headers = {
  'Content-Type': 'application/json'
}
    data = requests.get(url + "/string_test",headers=headers).text
    return data

def put(url):
    
    print("making put request to " + url+"/string_test")
    body = json.dumps({
  "name": "string_test25",
  "email": "blac_dev@email.com"
})
    headers = {
  'Content-Type': 'application/json'
}
    data = requests.put(url + "/string_test", data=body,headers=headers).text
    return data

def delete(url):
    print("making delete request to " + url+"/string_test25")
    headers = {
  'Content-Type': 'application/json'
}
    data = requests.delete(url + "/string_test25",headers=headers).text
    return data
if __name__ == "__main__":
    url = sys.argv[1]
    functions = [post, get, put, delete]
    # loop through 4 functions and pring out the results
    for i in functions:
        pprint(i(url))
