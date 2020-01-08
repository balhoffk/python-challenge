import csv
import os

file1 = os.path.join("Resources", "election_data.csv")
#Confirm analysis file with TA
file2 = os.path.join("analysisfile", "election_analysis.txt")
votecount = 0
candidates = []
candidatevotecount = {}
winningcandidate = ""
winningvotecount = 0

with open(file1) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader:

        votecount = votecount + 1
        name = row[2]
        if name not in candidates:
            candidates.append(name)
            candidatevotecount[name] = 0
        candidatevotecount[name] = candidatevotecount[name] + 1

#Break
with open(file2, "w") as txt_file:

    results = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {votecount}\n"
        f"----------------------\n")
    print(results, end="")

    txt_file.write(results)

    for winner in candidatevotecount:

        votes = candidatevotecount.get(winner)
        percentvote = float(votes) / float(votecount) * 100

        if (votes > winningvotecount):
            winningvotecount = votes
            winningcandidate = winner
        countandpercent = f"{winner}: {percentvote:.3f}% ({votes})\n"
        print(countandpercent, end="")
        txt_file.write(countandpercent)

    winningcandidatesummary = (
        f"----------------------\n"
        f"Winner: {winningcandidate}\n"
        f"----------------------\n")
    print(winningcandidatesummary)

    txt_file.write(winningcandidatesummary)