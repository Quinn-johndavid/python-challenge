import os 
import csv 
#input and output file paths
pollDataRead = "Resources/election_data.csv"
pollAnalysisOut = "Analysis/electionAnalysis.txt"
#array, dictionary and variable
totalVotes = 0
candidateNameStore = []
candidateVotes = {}

pollWinnerCandName = ""
pollWinCount = 0

#opens the filepath and then seperates the columns by comma's in the csv
with open(pollDataRead) as PDR:
    PDRReader = csv.reader(PDR,delimiter=",")

    #Added this line as it was counting the header in the summary, this line of code basically tells the computer to step through the line with headers and start at the first row of data (row2)
    header = next(PDRReader)

    for row in PDRReader:

        
#adds the votes to their respective candidate, and is directed to column2 
        totalVotes = totalVotes + 1

        candidateName = row[2]

#adds candidate if candidate is not in the name array, then sets their total vote count to 0 to initilize the variable and then for each time their name 
        if candidateName not in candidateNameStore:

            candidateNameStore.append(candidateName)

            candidateVotes[candidateName] = 0 
        candidateVotes[candidateName] = candidateVotes[candidateName] + 1

#Start of the Analysis
with open(pollAnalysisOut, "w") as analysisOut:

    pollResults = (
        
        f"\nElection Results\n\n"
        f"-----------------------\n\n"
        f"TotalVotes:{totalVotes}\n\n"
        f"------------------------\n"
    )
    print(pollResults)
    #quick summary of the poll results and outputs to terminal and then the analysis file 
    analysisOut.write(pollResults)

    for candidate in candidateVotes:
#grabs the amount of votes for each candidate, then calculates the perecentage of vote
        votes = candidateVotes.get(candidate)
        percentOfVote = float(votes)/float(totalVotes) *100

        if(votes >pollWinCount):
            pollWinCount = votes
            pollWinnerCandName = candidate

#strings together the candidate name, their percentage of the vote, and the actual amount of their votes, then prints to terminal and adds to the analysis file 
        pollOutput = f"{candidate}: {percentOfVote:.2f}% ({votes})\n"
        print(pollOutput)

        analysisOut.write(pollOutput)
    
    #Output variable, super cool
    summaryOfPollResults = (
        f"------------------------------\n"
        f"Winner: {pollWinnerCandName}\n"
        f"-----------------------------\n"
    )
    print(summaryOfPollResults)
    #writes the aforementioned output variable to the output file 
    analysisOut.write(summaryOfPollResults)