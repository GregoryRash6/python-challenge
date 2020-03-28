# Import Dependencies
import os
import csv
# Set Path for File
file_location = '../../../nu-chi-data-pt-03-2020-u-c/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'
# Variables
total = 0
khan = 0
correy = 0
li = 0
otooley = 0
# Open and Read CSV
with open(file_location, "r") as csvfile:
# Spli Data on Commas
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the Header
    csv_header = next(csvreader)
# Read each Line after the Header   
    for row in csvreader:
# Calculate Total Votes
        total += 1
#  Calculate Number of Votes for each Candidate               
        if (row[2] == "Khan"):
            khan += 1
        elif (row[2] == "Correy"):
            correy += 1
        elif (row[2] == "Li"):
            li += 1
        elif (row[2] == "O'Tooley"):
            otooley += 1
# Calculate Percentage of Votes for each Candidate   
    khan_percent = khan / total
    correy_percent = correy / total
    li_percent = li / total
    otooley_percent = otooley /total
# Find Candidate with the Most Votes
    election_winner = max(khan, correy, li, otooley)
# Designate the Candidate with the Most Votes as Election Winner 
    if election_winner == khan:
        winner = "Khan"
    elif election_winner == correy:
        winner = "Correy"
    elif election_winner == li:
        winner = "Li"
    elif election_winner == otooley:
        winner = "O'Tooley"
# Print Election Results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
print(f"Khan: {khan_percent:.3%} ({khan})")
print(f"Correy: {correy_percent:.3%} ({correy})")
print(f"Li: {li_percent:.3%} ({li})")
print(f"O'Tooley: {otooley_percent:.3%} ({otooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
# Specify Output Location 
output_file_location = "PyPoll"
# Write Election Results to Text File
with open(output_file_location, "w",) as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%} ({khan})\n")
    txtfile.write(f"Correy: {correy_percent:.3%} ({correy})\n")
    txtfile.write(f"Li: {li_percent:.3%} ({li})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%} ({otooley})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
