# -*- coding: utf-8 -*-
"""
sportsStats Main

1)Input players name, return link(s) in array
2) returns 0 array if not found
"""

'''

sportType: 
    'baseball':

'''

#for web scraping
from bs4 import BeautifulSoup
#for pulling site from web
import urllib.request

def getPlayerLink(sportType, playerFirstName, playerLastName):
    arrayIndex=0
    linkArray=[0]
    
    #Find first letter of lastName
    lNamefLetter=playerLastName[0]
    #fullPlayerTable for lNamefLetter
    playerPageLink='http://www.baseball-reference.com/players/'+lNamefLetter.lower()+"/"  
    
    #player full name
    playerfNamelName=playerFirstName+' '+playerLastName
    response = urllib.request.urlopen(playerPageLink)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    tempLinkList = soup.find_all('a', string=playerfNamelName)
    for link in tempLinkList:
        temp=str(link.get('href'))
        linkArray[arrayIndex]='http://www.baseball-reference.com/'+temp
        arrayIndex+=1
    print(linkArray)
    return linkArray
    
def main():
    getPlayerLink('baseball', 'David', 'Aardsma')
    
if __name__ == "__main__":
    main()