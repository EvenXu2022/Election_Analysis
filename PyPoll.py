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

file_to_save = os.path.join("Analysis","election_analysis.txt")
file_to_load = os.path.join("election_results.csv")

with open (file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

 

