#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:00:29 2018

@author: brettwang
"""



import json
import csv
#import urllib.parse
from urllib.request import Request, urlopen  # the lib that handles the url stuff
url = 'https://ghost.computer/cx/cc-global-pairs.json'
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
f = urlopen(req)

#f = open('/Users/brettwang/Desktop/JSON2CSV/cc-global-pairs.json', 'r')
datastore = json.load(f)
f.close()

#get all coins name in all exchange
entity_exchange = list(datastore.keys())
entity_token = set()
pair = []

for (exchange, tokens) in datastore.items():
    entity_token = entity_token.union(tokens.keys())
    for val in tokens.values():
        entity_token = entity_token.union(val)
entity_token = list(entity_token)


for (exchange, tokens) in datastore.items():
    for (token_A, token_B_list) in tokens.items():
        for i in range(0, len(token_B_list)):
            pair.append([exchange, token_A,token_B_list[i]])
            

with open('cc-global-pairs-entities.csv', 'w') as csvfile:
    fieldnames = ['Entity Name', 'Entity Type']
    mywriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    mywriter.writeheader() #write field name for first row
    for j in range(0, len(entity_exchange)):  
        mywriter.writerow({'Entity Name':entity_exchange[j],'Entity Type':'Exchange'})
    for i in range(0, len(entity_token)):
        mywriter.writerow({'Entity Name':entity_token[i],'Entity Type':'Token'})

with open('cc-global-pairs.csv', 'w') as csvfile:
    fieldnames = ['Exchange', 'Token Name A', 'Token Name B']
    mywriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    mywriter.writeheader() #write field name for first row
    for j in range(0, len(pair)):  
        mywriter.writerow({'Exchange': pair[j][0],'Token Name A': pair[j][1], 'Token Name B': pair[j][2]})
