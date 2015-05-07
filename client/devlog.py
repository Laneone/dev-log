import os
import json
import requests
import lxml

input_line = ""
roots = []

def newDict(l, r):
    roots.append({l: r})

while(input_line != "exit"):
    input_line = input("> ")
    if(input_line == "root"):
        print("--> Root Element")
        l_value = input("> Input L (key): ")
        if(l_value != ""):
            r_value = input("> Input R (value): ")
            if(r_value != ""):
                newDict(l_value, r_value)        
    elif(input_line == "list" or input_line == "ls"):
        print("--> List")
        print(json.dumps(roots))
    elif(input_line == "upload"):
        print("--> Upload")
        for i in roots:
            payload = {"data": json.dumps(i)}
            print("Sending: " + json.dumps(payload))
            response = requests.post("http://localhost:8080", data=payload)
            print(response.text.rstrip('\n'))
    elif(input_line == "download"):
        print("--> Download")
        page = int(input("> Input page: "))
        print(json.dumps(json.loads(requests.get("http://localhost:8080/?" + str(page)).text), sort_keys=True, indent=4))
    elif(input_line == "refresh"):
        roots = []
        print("--> Refreshed")
    elif(input_line == "help"):
        print("help\nroot\nlist\nupload\nrefresh\ndownload\nexit")

