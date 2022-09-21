#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:20:38 2022

@author: chatmongkolchuenteerawong
"""

import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = '/Users/chatmongkolchuenteerawong/Downloads/Data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader (f)
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index,column_header)
    
    long,las,fri = [],[],[]
    for row in reader:
        lon = float(row[0])
        lat=float(row[1])
        fr=float(row[2])
        long.append(lon)
        las.append(lat)
        fri.append(fr)
        
data = [{
        'type': 'scattergeo',
        'lon': las,
        'lat': long,
        'marker': {
            'size': [0.03*fr for fr in fri],
            'color': fri,
            'colorscale': 'reds',
            'reversescale': True,
            'colorbar': {'title': 'world fire'},
            },
        }]
    
my_layout = Layout(title='Global World Fire')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_kkk.html')
#test



