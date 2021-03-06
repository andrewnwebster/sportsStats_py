# -*- coding: utf-8 -*-
"""
returns dictionary of hitting or pitching stats
"""

#for web scraping
from bs4 import BeautifulSoup
#for pulling site from web
import urllib.request
import sys
import re

def cleanStats(statsClass, statsTemplate, rawBSstats):
    statsDict={}

    batting_standard_re = 'batting_standard\.((18|19|20)[0-9]{2})'
    pitching_standard_re = 'pitching_standard\.((18|19|20)[0-9]{2})'
    stats_standard_re=''

    if statsClass == 0:
        stats_standard_re=batting_standard_re
    elif statsClass == 1:
        stats_standard_re=pitching_standard_re

    stats = []
    batting_table_body = rawBSstats.findAll('tbody')[0]
    for table_row in batting_table_body.findAll('tr'):
        #print(table_row)
        table_row_id = table_row.get('id')
        #print(table_row_id)

        if not table_row_id:
            continue
        year = re.findall(stats_standard_re, table_row_id)
        
        row_values = {}
        
        headers = {element.get('data-stat'):element.text for element in table_row.findAll('td')}
        values = [element.text for element in table_row.findAll('td')]

        #<-- stats year and dict
        #print(year[0][0])
        #print(headers)

        statsDict[year[0][0]]=headers
    return statsDict