import os
import csv
cvspath=os.path.join("Resources","budget_data.csv")
with open (cvspath) as csvfile:
	csvreader=csv.reader(csvfile,delimiter=',')
	csv_header=next(csvreader)
	total_months=0
	profit=0
	change=0
	maxincrease=0
	maxdecrease=0
	prevrow1=0
	sumofchange=0
	x=0
	for row in csvreader:
		x=x+1
		total_months=total_months+1
		profit=profit+int(row[1])
		change=int(row[1])-prevrow1
		if x>1:
			sumofchange=sumofchange+change
		if change>0:
			increase=change
			if increase>maxincrease:
				maxincrease=increase
				DateMax=row[0]
		elif change<0:
			decrease=change
			if decrease<maxdecrease:
				maxdecrease=decrease
				DateMin=row[0]
		prevrow1=int(row[1])
	averagechange=round(sumofchange/(total_months-1),2)
	
		
		
	print('-----------------------------------')
	print(f'Financial Analysis')
	print('-----------------------------------')
	print(f'Total Months: {total_months}')
	print(f'Total: ${profit}')
	print(f'Average change: ${averagechange}')
	print(f'The greatest increase in profits : {DateMax}  $({maxincrease})')
	print(f'The greatest decrease in profits : {DateMin}  $({maxdecrease})')
	print('-----------------------------------')
	filepath=os.path.join("analysis/PyBank_Data_Analysis_Results.txt")
	with open(filepath,"w") as file:
		file.write("-----------------------------------\nFinancial Analysis\n-----------------------------------\nTotal Months: "+str(total_months)+'\nTotal: $'+str(profit)+'\nAverage change: $'+str(averagechange)+'\nThe greatest increase in profits : '+str(DateMax) + ' $('+str(maxincrease)+")\nThe greatest decrease in profits : "+str(DateMin) + ' $('+str(maxdecrease)+')\n-----------------------------------')
		file.close()  
	
