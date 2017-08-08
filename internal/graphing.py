import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def plotStats(playerType, statsDF, dfColumns):
	multiplotChart(playerType, statsDF, dfColumns)

def multiplotChart(playerType, statsDF, dfColumns):
	params={
		'x':'year',
		'y':['',''],
	}

	if playerType==0:
		params['y']=['HR','RBI']
	elif playerType==1:
		params['y']=['k','era']
	else:
		print('something went wrong')
		return 0

	x_key=params['x']
	y_key=params['y']

	tempDF=statsDF

	tempDF[x_key]=statsDF[x_key].astype(int)
	xValue=tempDF[x_key]
	yValue=[statsDF[y].astype(float) for y in y_key]

	temp_dict = [sorted(dict(zip(xValue, y)).items()) for y in yValue]

	graph_1=temp_dict[0]
	graph_2=temp_dict[1]

	x,y=zip(*graph_1)
	u,v=zip(*graph_2)

	fig, ax1 = plt.subplots()

	if playerType==0:
		ax1.plot(x,y, 'b-')
		ax1.set_xlabel('year')
		ax1.set_ylabel('HR')
		ax2=ax1.twinx()
		ax2.plot(u,v, 'r-')
		ax2.set_ylabel('RBI')
	elif playerType==1:
		ax1.plot(x,y, 'b-')
		ax1.set_xlabel('year')
		ax1.set_ylabel('k')
		ax2=ax1.twinx()
		ax2.plot(u,v, 'r-')
		ax2.set_ylabel('era')
	else:
		print('graphing went wrong')
		return 0
	


	plt.xticks(x,x)
	fig.tight_layout()
	plt.show()

	
def singleVariableChart(playerType, statsDF, dfColumns):

	params={
			'x':'year',
			'y':'',
				}

	if playerType==0:
		params['y']='RBI'
	elif playerType==1:
		params['y']='era'
	else:
		print('something went wrong')
		return 0

	x_key=params['x']
	y_key=params['y']

	tempDF=statsDF
	tempDF[x_key]=statsDF[x_key].astype(int)
	tempDF[y_key]=statsDF[y_key].astype(float)
	xValue=tempDF[x_key]
	yValue=tempDF[y_key]

	temp_dict = dict(zip(xValue, yValue))
	temp_dict = sorted(temp_dict.items())
	x,y = zip(*temp_dict)
	plt.plot(x,y)
	plt.xticks(x,x)
	plt.show()