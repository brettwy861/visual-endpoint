#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:18:59 2018

@author: brettwang
"""

import json
import csv
f = open('/Users/brettwang/Desktop/JSON2CSV/cc-global-pairs.json', 'r')
#json.dump(obj, f, *, skipkeys=True, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
datastore = json.load(f)
f.close()

#get all coins name in all exchange
entity_exchange = list(datastore.keys())
entity_token = set()
for item in datastore.items():
    item = item[1]
    entity_token = entity_token.union(item.keys())
    for val in item.values():
        entity_token = entity_token.union(val)
entity_token = list(entity_token)

with open('cc-global-pairs-entities.csv', 'w') as csvfile:
    fieldnames = ['Entity Name', 'Entity Type']
    mywriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    mywriter.writeheader() #write field name for first row
    for j in range(0, len(entity_exchange)):  
        mywriter.writerow({'Entity Name':entity_exchange[j],'Entity Type':'Exchange'})
    for i in range(0, len(entity_token)):
        mywriter.writerow({'Entity Name':entity_token[i],'Entity Type':'Token'})
        
        