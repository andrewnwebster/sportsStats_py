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

def shortenedStats(playerType, statsDF):
	shortenedColumnGroup=[]
	shortenedHitterStatsList=[
		'year',
		'G',
		'AB',
		'H',
		'R',
		'2B',
		'3B',
		'HR',
		'RBI',
		'avg',
		'ops',
		'age',
	]

	shortenedPitcherStatsList=[
		'year',
		'G', 
		'GS', 
		'IP',  
		'SV', 
		'W', 
		'L', 
		'era',
		'whip',
		'k',
		'k/9',
		'k/bb',
		]

	if playerType==0:
		shortenedColumnGroup=shortenedHitterStatsList
	elif playerType==1:
		shortenedColumnGroup=shortenedPitcherStatsList
	else:
		return

	finalDF=statsDF[shortenedColumnGroup]
	
	return finalDF

def changeNamesOfStas(playerType,statsDF):
	
	renameKeysHitters={
		#'2B', 
		#'3B', 
		#'AB', 
		#'BB', 
		#'CS', 
		#'G', 
		#'GIDP', 
		#'H', 
		#'HBP', 
		#'HR', 
		#'IBB', 
		#'PA', 
		#'R', 
		#'RBI', 
		#'SB', 
		#'SF', 
		#'SH', 
		#'SO', 
		#'TB', 
		#'age', 
		'award_summary':'awds', 
		'batting_avg':'avg', 
		'lg_ID':'lge', 
		'onbase_perc':'obp', 
		'onbase_plus_slugging':'ops', 
		'onbase_plus_slugging_plus':'ops+', 
		'pos_season':'plyoff', 
		'slugging_perc':'slg', 
		'team_ID':'team', 
		#'year'
	}
	
	renameKeysPitchers={
		#'B', 
		#'BK', 
		#'CG', 
		#'ER', 
		#'G', 
		#'GF', 
		#'GS', 
		#'H', 
		#'HBP', 
		#'HR', 
		#'IBB', 
		#'IP', 
		#'L', 
		#'R', 
		#'SHO', 
		'SO':'k', 
		#'SV', 
		#'W', 
		#'WP', 
		#'age', 
		'award_summary':'awds', 
		'bases_on_balls_per_nine':'bb/9', 
		'batters_faced':'bf', 
		'earned_run_avg':'era', 
		'earned_run_avg_plus':'era+', 
		#'fip', 
		'hits_per_nine':'h/9', 
		'home_runs_per_nine':'hr/9', 
		'lg_ID':'lge', 
		'strikeouts_per_base_on_balls':'k/bb', 
		'strikeouts_per_nine':'k/9', 
		'team_ID':'team', 
		#'whip', 
		'win_loss_perc':'wl%', 
		#'year'
	}

	if playerType==0:
		renameColumnGroup=renameKeysHitters
	elif playerType==1:
		renameColumnGroup=renameKeysPitchers
	else:
		return
	
	finalDF=statsDF.rename(index=str, columns=renameColumnGroup)

	return finalDF
	