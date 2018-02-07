#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:14:32 2018

@author: brettwy861
"""

"""
write JSON in the tree format, with keys ["names","parent","children"]
"""
import ccxt  # noqa: E402
import json

def add_newchildren(dictitem, name):
    
    if type(dictitem) is dict:
        children_dict = []
#        children_dict['children'] = []
        for item in dictitem.keys():
            newnode = {}
            newnode['name'] = item
            newnode['parent'] = name
            newnode['children'] = add_newchildren(dictitem[item], newnode['name'])
            children_dict.append(newnode)
        return children_dict
    elif type(dictitem) is list:
        children_dict = []
        for item in dictitem:
            newnode = {}
            newnode['name'] = item
            newnode['parent'] = name
            children_dict.append(newnode)
        return children_dict
    else:
        print('dictitem not dict or list or str')
        return 0
        
exchange_list = ccxt.exchanges

for name in exchange_list:
    exchange = ccxt.__dict__[name]({
    "apiKey": "",
    "secret": "",
    "enableRateLimit": True,
    })
    data = exchange.api
    new_dict = {}
    l = len(data.keys())
    new_dict['name'] = 'hitbtc2'
    new_dict['parent'] = 'null'
    new_dict['children'] = [] #append dicts to this list
    for item in data.keys():
        newnode = {}
        newnode['name'] = item #name of newnode is key of old node
        newnode['parent'] = new_dict['name']
        if type(data[item]) is not str:
            newnode['children'] = add_newchildren(data[item], newnode['name'])        
        new_dict['children'].append(newnode) 
    
    with open(name+'.json', 'w') as f:
        json.dump(new_dict, f, sort_keys=False, indent = 2)

    

