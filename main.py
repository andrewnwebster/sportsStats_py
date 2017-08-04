from links import getStats
from links import cleanStats
from clss import statsTemplate
from clss import statsClass
import sys

def main():
    statsList=()
    temp=getStats.getStats('David Aardsma','https://www.baseball-reference.com/players/a/aardsda01.shtml')
    tempClass=statsClass.statsClass[temp[0]]
    if tempClass == 0:
        statsList=statsTemplate.battingStats()
    elif tempClass == 1:
        statsList=statsTemplate.pitchingStats()


    tempStats=temp[1]
    #just for printing
    temp_raw=(tempStats.encode(sys.stdout.encoding, errors='replace'))
    
    temp_clean=cleanStats.cleanStats(tempClass, statsList, tempStats)
    print(temp_clean)
    print(tempClass)

if __name__ == "__main__":
    main()