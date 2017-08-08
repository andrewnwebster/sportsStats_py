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
import re

def getPlayerNameFromUser(fNamelNameList):
    tempList=['','']
    pattern = r'[A-Za-z]+'

    while True:
        tempList[0]=input('first name?')
        tempList[1]=input('last name?')

        fName=tempList[0]
        lName=tempList[1]
    
        if re.match(pattern, fName) and re.match(pattern, lName):
            return tempList
        else:
            print('tryAgain')

def getPlayerLink(sportType, playerFirstName, playerLastName):
    arrayIndex=0
    linkArray=[]
    
    #Find first letter of lastName
    lNamefLetter=playerLastName[0]
    #fullPlayerTable for lNamefLetter
    playerPageLink='https://www.baseball-reference.com/players/'+lNamefLetter.lower()+"/"  
    
    #player full name
    playerfNamelName=playerFirstName+' '+playerLastName
    response = urllib.request.urlopen(playerPageLink)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    tempLinkList = soup.find_all('a', string=playerfNamelName)
    for link in tempLinkList:

        temp=str(link.get('href'))
        print(temp)
        linkArray.extend(['http://www.baseball-reference.com/'+temp])
        arrayIndex+=1
    return linkArray[0]