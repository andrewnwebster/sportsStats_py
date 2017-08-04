# -*- coding: utf-8 -*-
"""
"""

#for web scraping
from bs4 import BeautifulSoup
#for pulling site from web
import urllib.request
import sys
import re

def cleanStats(statsClass, statsTemplate, rawBSstats):
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
        table_row_id = table_row.get('id')
        if not table_row_id:
            continue
        year = re.findall(stats_standard_re, table_row_id)
        row_values = {}
        values = [element.text for element in table_row.findAll('td')]
        my_keys_with_values = zip(statsTemplate, values)
        row_values = dict(my_keys_with_values)

        stats.append(row_values)
    return stats