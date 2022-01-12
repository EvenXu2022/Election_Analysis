counties = ["Arapahoe","Denver","Jefferson"]
    

"""for i in range(len(counties)):
    print(counties[i])"""

"""counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(counties_dict.get(county))

for Key, value in counties_dict.items():
    print(str(Key) + " county has " + str(value) + " registered voters")"""

"""if counties[1]=='Denver':
    print(counties[1])
temperature = int(input("what is the temperature outside?"))
if temperature >80:
    print("turn on the AC")
else:
    print("open the windows")

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
"""
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

"""for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])"""

"""for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:

     print(county_dict['county'])"""

"""counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print (f"{county} county has {voters} registered voters.")"""

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for i in range(len(counties)):
    print (counties[i])

# election_data = open('election_results.csv', mode = 'w')
# print (election_data)

# with open ('election_results.csv') as election_data:
#     print (election_data)
# print(dir(os))

 #  for row in file_reader:
#      print(row[0])

# outfile= open(file_to_save,'w')
# outfile.write("Hello World")
# outfile.close()

#with open(file_to_save, 'w') as txt_file:

#    txt_file.write("Countis in the Election\n-------------------\nArapahoe\nDenver\nJefferson") #3.4

