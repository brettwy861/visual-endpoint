#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:57:01 2018
@author: brettwang
"""

import json
import xlsxwriter
from urllib.request import Request, urlopen  # the lib that handles the url stuff
url = 'https://ghost.computer/cx/icolist-all.json'
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
f = urlopen(req)
datastore = json.load(f)
f.close()

data_sheet1 = datastore['ico']['live']
data_sheet2 = datastore['ico']['upcoming']
data_sheet3 = datastore['ico']['finished']

workbook = xlsxwriter.Workbook('icolist-all-three-sheets.xlsx')            
worksheet1 = workbook.add_worksheet('icolist-live')
worksheet2 = workbook.add_worksheet('icolist-upcoming')
worksheet3 = workbook.add_worksheet('icolist-finished')

worksheet1.write_row(0, 0, data_sheet1[0].keys())
worksheet2.write_row(0, 0, data_sheet2[0].keys())
worksheet3.write_row(0, 0, data_sheet3[0].keys())

for counter, item in enumerate(data_sheet1):
    worksheet1.write_row(counter+1, 0, item.values())   
for counter, item in enumerate(data_sheet2):
    worksheet2.write_row(counter+1, 0, item.values()) 
for counter, item in enumerate(data_sheet3):
    worksheet3.write_row(counter+1, 0, item.values()) 
    
workbook.close()
