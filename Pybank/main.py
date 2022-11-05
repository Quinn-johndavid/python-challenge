import os
import csv

# Path to collect data from the Resources folder
budgetDataRead = "Resources/budget_data.csv"
budgetDataAnalysis = "Analysis/budgetData.txt"

totalMonths = []
totalProfit = []
monthlyPChange = []

with open (budgetDataRead) as BDR:
    BDR_reader = csv.reader(BDR,delimiter=",")
    bdrHeader = next(BDR_reader)

    for row in BDR_reader:

        totalMonths.append(row[0])
        totalProfit.append(int(row[1]))


    for i in range(len(totalProfit)-1):

        monthlyPChange.append(totalProfit[i+1]-totalProfit[i])

maxProfit = max(monthlyPChange)
minProfit = min(monthlyPChange)
monthlyMaxProfit = monthlyPChange.index(max(monthlyPChange)) + 1 
monthlyMinProfit = monthlyPChange.index(min(monthlyPChange)) + 1


 
""" print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(totalMonths)}")
print(f"Total Revenue: ${sum(totalProfit)}")
print(f"Average Revenue Change: ${round(sum(monthlyPChange)/len(monthlyPChange),2)}")
print(f"Greatest Increase in Profits: {totalMonths[monthlyMaxProfit]} ${(str(maxProfit))}")
print(f"Greatest Decrease in Profits: {totalMonths[monthlyMinProfit]} ${(str(minProfit))}")
 """
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

with open(budgetDataAnalysis, "w") as endfile:
    endfile.write(output)