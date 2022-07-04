from links import getStats
from links import cleanStats
from links import getPlayerLink as gpl
from clss import statsTemplate
from clss import statsClass
import pandas as pd
from internal import statsDictToDF as sdf
from internal import graphing as grp
import sys



def main():

    statsList=()
    playerName=[]


    userInputPlayerName=gpl.getPlayerNameFromUser(playerName)
    generatedPlayerLink=gpl.getPlayerLink('baseball', userInputPlayerName['fname'], userInputPlayerName['lname'])
    temp=getStats.getStats(userInputPlayerName['fname']+' '+userInputPlayerName['lname'],generatedPlayerLink)

    #(Batter or Pitcher, then statsDF)
    #TO DO: Change to getting batter and pitcher stats -- and a flag if empty
    tempClass=statsClass.statsClass[temp[0]]
    tempClassID=temp[0]
    if tempClassID == 0:
        statsList=statsTemplate.battingStats()
    elif tempClassID == 1:
        statsList=statsTemplate.pitchingStats()

    tempStats=temp[1]

    temp_raw=(tempStats.encode(sys.stdout.encoding, errors='replace'))
    temp_clean_dict=cleanStats.cleanStats(tempClassID, statsList, tempStats)
    temp_clean_DF=sdf.statsDictToDF(temp_clean_dict)
    renamed_stats_DF=sdf.changeNamesOfStas(tempClassID,temp_clean_DF)
    shortened_stats_DF=sdf.shortenedStats(tempClassID,renamed_stats_DF)

    print(shortened_stats_DF.to_string(index=False))
    grp.plotStats(tempClassID, renamed_stats_DF, list(renamed_stats_DF))

if __name__ == "__main__":
    main()