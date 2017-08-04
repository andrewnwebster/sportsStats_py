# -*- coding: utf-8 -*-
"""
sportsStats Main

1)Input player link, from getPlayerLink
2)Outputs:
    IDEAL: career stats
    BACKUP: current year, past years can be bought and stored (not preferable)
"""

#for web scraping
from bs4 import BeautifulSoup
#for pulling site from web
import urllib.request
import sys

def getStats(playerNamePretty, playerLink):
    response = urllib.request.urlopen(playerLink)
    html = response.read()
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    counter=0

    for table in soup.findAll('table'):
        #print(table.encode(sys.stdout.encoding, errors='replace'))
        #print('\n\n\n\n\n')
        counter+=1
        try:
            if table['id'] == 'batting_standard':
                return (0,table)
            elif table['id'] == 'pitching_standard':
                return (1,table)
            else:
                pass
        except keyError:
            pass
    print('meh')
    print(counter)