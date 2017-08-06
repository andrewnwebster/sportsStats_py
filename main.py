from links import getStats
from links import cleanStats
from clss import statsTemplate
from clss import statsClass
import pandas as pd
from internal import statsDictToDF as sdf
import sys

def main():
    statsList=()
    temp=getStats.getStats('Derek Jeter','https://www.baseball-reference.com/players/j/jeterde01.shtml')
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

    print(list(temp_clean_DF))

if __name__ == "__main__":
    main()