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

#f = open('/Users/brettwang/Desktop/JSON2CSV/cc-global-pairs.json', 'r')
datastore = json.load(f)
f.close()


workbook = xlsxwriter.Workbook('cc-global-pairs-two-sheets-spreadsheet.xlsx')            
worksheet1 = workbook.add_worksheet('cc-global-pairs-entities')
worksheet2 = workbook.add_worksheet('cc-global-pairs')

#get all coins name in all exchange
entity_exchange = list(datastore.keys())
entity_token = set()
pair = []


for (exchange, tokens) in datastore.items():
    entity_token = entity_token.union(tokens.keys())
    for val in tokens.values():
        entity_token = entity_token.union(val)
entity_token = list(entity_token)

row = 0
worksheet1.write(row, 0, 'Entity Name')
worksheet1.write(row, 1, 'Entity Type')
for j in range(0, len(entity_exchange)):
    row = row + 1
    worksheet1.write(row, 0, entity_exchange[j])
    worksheet1.write(row, 1, 'Exchange')
        #mywriter.writerow({'Entity Name':entity_exchange[j],'Entity Type':'Exchange'})
    
for i in range(0, len(entity_token)):
        #mywriter.writerow({'Entity Name':entity_token[i],'Entity Type':'Token'})
    row = row + 1
    worksheet1.write(row, 0, entity_token[i])
    worksheet1.write(row, 1, 'Token')

row = 0
worksheet2.write(row, 0, 'Exchange')
worksheet2.write(row, 1, 'Token Name A')
worksheet2.write(row, 2, 'Token Name B')
for (exchange, tokens) in datastore.items():
    for (token_A, token_B_list) in tokens.items():
        for i in range(0, len(token_B_list)):
            #pair.append([exchange, token_A,token_B_list[i]])
            row = row + 1
            worksheet2.write(row, 0, exchange) 
            worksheet2.write(row, 1, token_A)
            worksheet2.write(row, 2, token_B_list[i])
            



workbook.close()

"""
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
"""