#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:00:29 2018

@author: brettwang
"""



import json
import xlsxwriter
from urllib.request import Request, urlopen  # the lib that handles the url stuff
url = 'https://ghost.computer/cx/cc-global-pairs.json'
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
f = urlopen(req)
datastore = json.load(f)
f.close()


workbook = xlsxwriter.Workbook('cc-global-pairs-two-sheets-spreadsheet-faster.xlsx')            
worksheet1 = workbook.add_worksheet('cc-global-pairs-entities')
worksheet2 = workbook.add_worksheet('cc-global-pairs')


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

worksheet2.write_row(0, 0, ['Exchange','Token Name A','Token Name B'])
for row in range(0,len(pair)):
    worksheet2.write_row(row+1, 0, pair[row]) 
    

worksheet1.write_row(0, 0, ['Entity Name','Entity Type'])
worksheet1.write_column(1,0, entity_exchange)
worksheet1.write_column(1,1,['Exchange']*len(entity_exchange))
worksheet1.write_column(len(entity_exchange)+1,0,entity_token)
worksheet1.write_column(len(entity_exchange)+1,1,['Token']*len(entity_token))

workbook.close()