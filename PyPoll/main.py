import os
import csv
csvpath=os.path.join('Resources/election_data.csv')
with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile,delimiter=',')
	cvsheader=next(csvreader)
	total=0
	candidatelist=[]
	candidatecount=[]
	candidatepercent=[]
	x=0
	for row in csvreader:
		total=total+1
		newcandidate=row[2]
		while x==0:
			candidatelist.append(newcandidate)
			candidatecount.append(1)
			candidatepercent.append(0)
			x=x+1
		if newcandidate in candidatelist:
			index=candidatelist.index(newcandidate)
			candidatecount[index]=candidatecount[index]+1
		else:
			candidatelist.append(newcandidate)
			candidatecount.append(1)
			candidatepercent.append(0)
	for i in range(len(candidatelist)):
		candidatepercent[i]=round((candidatecount[i]/sum(candidatecount)*100),1)
	print('Election Results')
	print('---------------------------')
	print(f'Total Votes: {total}')
	print('---------------------------')
	filepath=os.path.join("analysis/PyPol_Data_Analysis_Results.txt")
	with open(filepath,"w") as file:
		file.write("\nElecttion Results\n-----------------------------------\nTotal Votes: "+str(total)+'\n-----------------------------------\n') 
	
	for name in candidatelist:
		index=candidatelist.index(name)
		count=candidatecount[index]
		percent=candidatepercent[index]
		print(f'{name}:		{percent}%   ({count})')
		filepath=os.path.join("analysis/PyPol_Data_Analysis_Results.txt")
		with open(filepath,"a") as file:
			file.write('\n'+str(name)+":		"+str(percent)+"%   ("+str(count)+")\n")
			file.close()
	print('---------------------------')
	maxvote=max(candidatecount)
	indexmaxvote=candidatecount.index(maxvote)
	winnername=candidatelist[indexmaxvote]
	print(f'Winner:{winnername}')
	print('---------------------------')

filepath=os.path.join("analysis/PyPol_Data_Analysis_Results.txt")
with open(filepath,"a") as file:
	file.write('---------------------------\nWinner:'+str(winnername))
	file.close()
	