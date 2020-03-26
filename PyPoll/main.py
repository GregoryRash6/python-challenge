import os
import csv

file_location = '../../../nu-chi-data-pt-03-2020-u-c/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'

total = 0
khan = 0
correy = 0
li = 0
otooley = 0

with open(file_location, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
   
    for row in csvreader:

        total += 1
        
        if (row[2] == "Khan"):
            khan += 1
        elif (row[2] == "Correy"):
            correy += 1
        elif (row[2] == "Li"):
            li += 1
        elif (row[2] == "O'Tooley"):
            otooley += 1
    
    khan_percent = khan / total
    correy_percent = correy / total
    li_percent = li / total
    otooley_percent = otooley /total

    election_winner = max(khan, correy, li, otooley)

    if election_winner == khan:
        winner = "Khan"
    elif election_winner == correy:
        winner = "Correy"
    elif election_winner == li:
        winner = "Li"
    elif election_winner == otooley:
        winner = "O'Tooley"

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

output_file_location = "PyPoll"

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
