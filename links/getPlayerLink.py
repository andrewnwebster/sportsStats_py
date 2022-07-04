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
import sys

def getPlayerNameFromUser(fNamelNameList):
    playerNameDict={'fname':'','lname':''}
    pattern = r'[A-Za-z]+'

    while True:
        playerNameDict['fname']=input('first name?')
        playerNameDict['lname']=input('last name?')

        fName=playerNameDict['fname']
        lName=playerNameDict['lname']
    
        if re.match(pattern, fName) and re.match(pattern, lName):
            return playerNameDict
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

    for item in soup.find_all('a', string=playerfNamelName):
        print(item)
        for link in item.find_all('a'):
            print(link.get('href'))

    print('Test')
    for item in soup.find_all('p', playerfNamelName):
        print(item)
    print('End Test')

    tempLinkList = soup.find_all('a', string=playerfNamelName)
    tempLinkList = removeDuplicatesFromList(tempLinkList)
    for link in tempLinkList:
        temp=str(link.get('href'))
        linkArray.extend(['http://www.baseball-reference.com/'+temp])
        arrayIndex+=1

    linkArray=removeDuplicatesFromList(linkArray)

    print('Array Contents | {0}'.format(linkArray))
    print('Length | {0}'.format(len(linkArray)))

    if len(linkArray) == 1:
        return linkArray[0]
    elif len(linkArray) == 0:
        print('Bad Link Count {0} in getPlayerLink'.format(len(linkArray)))
        sys.exit()
    else:
        chooseFromList(linkArray)
        return linkArray[0]

def chooseFromList(x):
    print('Please Choose Player')
    pass
        
def removeDuplicatesFromList(x):
    #print(list(dict.fromkeys(x)))
    return list(dict.fromkeys(x))

