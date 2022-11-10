import os
import csv

# Path to collect data from the Resources folder
budgetDataRead = "Resources/budget_data.csv"
#Path to output analysis
budgetDataAnalysis = "Analysis/budgetData.txt"

totalMonths = []
totalProfit = []
monthlyPChange = []
#opens the csv and seperates the collumns based on the headers ,'s then skips the header for rowcounting purposes, without there would be 4 candidates in the list one of them being "candidate" with 0 votes
with open (budgetDataRead) as BDR:
    BDR_reader = csv.reader(BDR,delimiter=",")
    bdrHeader = next(BDR_reader)
#adds the values from the first column in the csv and adds it to its respective array
    for row in BDR_reader:

        totalMonths.append(row[0])
        totalProfit.append(int(row[1]))


    for i in range(len(totalProfit)-1):

        monthlyPChange.append(totalProfit[i+1]-totalProfit[i])
#Finds the min and max of the monthlyPchange array and then 
#Correlate max and min to the proper month using month list and index associated 
#+ 1 at the end since month associated with change is the next month
maxProfit = max(monthlyPChange)
minProfit = min(monthlyPChange)
monthlyMaxProfit = monthlyPChange.index(max(monthlyPChange)) + 1 
monthlyMinProfit = monthlyPChange.index(min(monthlyPChange)) + 1


 #Sloppy, left out in the open, output variables are the way to go
""" print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(totalMonths)}")
print(f"Total Revenue: ${sum(totalProfit)}")
print(f"Average Revenue Change: ${round(sum(monthlyPChange)/len(monthlyPChange),2)}")
print(f"Greatest Increase in Profits: {totalMonths[monthlyMaxProfit]} ${(str(maxProfit))}")
print(f"Greatest Decrease in Profits: {totalMonths[monthlyMinProfit]} ${(str(minProfit))}")
 """

#Output Variables are amazing
output = (
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {len(totalMonths)}\n"
    f"Total Revenue: ${sum(totalProfit)}\n"
    f"Average Revenue Change: ${round(sum(monthlyPChange)/len(monthlyPChange),2)}\n"
    f"Greatest Increase in Profits: {totalMonths[monthlyMaxProfit]} ${(str(maxProfit))}\n"
    f"Greatest Decrease in Profits: {totalMonths[monthlyMinProfit]} ${(str(minProfit))}\n"

)

print(output)
#Writes final analysis to Analysis file
with open(budgetDataAnalysis, "w") as endfile:
    endfile.write(output)