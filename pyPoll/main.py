import os 
import csv 

pollDataRead = "Resources/election_data.csv"
pollAnalysisOut = "Analysis/electionAnalysis.txt"

totalVotes = 0
candidateNameStore = []
candidateVotes = {}

pollWinnerCandName = ""
pollWinCount = 0

with open(pollDataRead) as PDR:
    PDRReader = csv.reader(PDR,delimiter=",")

    #Added this line as it was counting the header in the summary, this line of code basically tells the computer to step through the line with headers and start at the first row of data (row2)
    header = next(PDRReader)

    for row in PDRReader:

        

        totalVotes = totalVotes + 1

        candidateName = row[2]


        if candidateName not in candidateNameStore:

            candidateNameStore.append(candidateName)

            candidateVotes[candidateName] = 0 
        candidateVotes[candidateName] = candidateVotes[candidateName] + 1

with open(pollAnalysisOut, "w") as analysisOut:

    pollResults = (
        
        f"\nElection Results\n\n"
        f"-----------------------\n\n"
        f"TotalVotes:{totalVotes}\n\n"
        f"------------------------\n"
    )
    print(pollResults)

    analysisOut.write(pollResults)

    for candidate in candidateVotes:

        votes = candidateVotes.get(candidate)
        percentOfVote = float(votes)/float(totalVotes) *100

        if(votes >pollWinCount):
            pollWinCount = votes
            pollWinnerCandName = candidate


        pollOutput = f"{candidate}: {percentOfVote:.2f}% ({votes})\n"
        print(pollOutput)

        analysisOut.write(pollOutput)
    
    summaryOfPollResults = (
        f"------------------------------\n"
        f"Winner: {pollWinnerCandName}\n"
        f"-----------------------------\n"
    )
    print(summaryOfPollResults)

    analysisOut.write(summaryOfPollResults)