import pandas as pd

def statsDictToDF(statsDict):
	statsDF=pd.DataFrame()

	for key,value in statsDict.items():
		temp = pd.DataFrame.from_dict([value], orient='columns')
		temp['year']=key
		statsDF=pd.concat([statsDF, temp], axis=0, ignore_index=True)

	statsDF['year'] = statsDF['year'].astype('int')
	statsDF=statsDF.sort_values(by='year')
	statsDF = statsDF.reset_index(drop=True)

	return statsDF