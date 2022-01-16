# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winder of the election based on popular vote

import datetime
# now = datetime.datetime.now()
# print ("The time right now is ", now)

import csv
import os

# Assign a variable to load a file from a path.
file_to_save = os.path.join("Analysis","election_analysis.txt")
# Assign a variable to save the file to a path.
file_to_load = os.path.join("election_results.csv")

# Initialize a total vote counter.
total_votes=0

# create Candidate options as list and candidate votes as dictionary
candidate_options = []
candidate_votes = {}

# Create variables : winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes +=1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# save the resutls to text file
with open (file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end = "")
    #write election_results to txt file
    txt_file.write(election_results)
#
# calculate vote count and percentage.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        #Print each candidate, their vote count, and percentage
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
#Find winning vote count winning percentage and candinate name
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

# print winning summary to the terminal
    winning_candidate_summary = (
        f"------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"
        f"winning percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------------\n"
        )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)















 

