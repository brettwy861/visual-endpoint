#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:57:01 2018
@author: brettwang
"""
import json
import csv
f = open('/Users/brettwang/Desktop/JSON2CSV/icolist-upcoming.json', 'r')
#json.dump(obj, f, *, skipkeys=True, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
datastore = json.load(f)
f.close()

while type(datastore) is dict:
# check main dict
    maxlen = 0
    for key in datastore.keys():
        if type(datastore[key]) is int:
            dictlen = 1
        else:
            dictlen = len(datastore[key])
        if dictlen >= maxlen:
            maxlen = dictlen
            data = datastore[key]
                   
    # check if the main dict has any subdict.
        datastore = data  


with open('icolist-upcoming.csv', 'w') as csvfile:
    fieldnames = list(datastore[0].keys())
    mywriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    mywriter.writeheader() #write field name for first row
    for i in range(0, len(datastore)):
        mywriter.writerow(datastore[i])
