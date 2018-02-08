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

pair = []
for (exchange, tokens) in datastore.items():
    for (token_A, token_B_list) in tokens.items():
        for i in range(0, len(token_B_list)):
            pair.append([exchange, token_A,token_B_list[i]])

with open('cc-global-pairs.csv', 'w') as csvfile:
    fieldnames = ['Exchange', 'Token Name A', 'Token Name B']
    mywriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    mywriter.writeheader() #write field name for first row
    for j in range(0, len(pair)):  
        mywriter.writerow({'Exchange': pair[j][0],'Token Name A': pair[j][1], 'Token Name B': pair[j][2]})
