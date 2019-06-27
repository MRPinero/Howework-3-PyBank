#DEPENDENCIES
import os #this line work
import csv #this line work

voter_id = []
county = []
candidate = []

#READ CVS FILE
election_data = os.path.join('..', '..', 'python-challenge', 'PyPoll', 'election_data.csv') 
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row_count = 0
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
#print(*voter_id, sep = "\n")       
#print(csvreader)

#FIND TOTAL NUMBER OF VOTES CAST
#election_data = list(csvreader)

#election_data = [r for r in csvreader]
print ("Election_Results")
print ("___________________________________________")
print ("Total_number_of_votes:", len(voter_id))
print ("___________________________________________")

#LIST OF CANDIDATES
List_of_candidates = set(["Khan", "Correy", "Li", "O'Tooley"])
candidate1 = "Khan"
Total_of_votes_Khan = candidate.count(candidate1)
print("Khan:", ((Total_of_votes_Khan/(len(candidate)*100), Total_of_votes_Khan)

    List_of_candidates = "Correy"
    candidate2 = "Correy"
    Total_of_votes_Correy = candidate.count(candidate2)
    print("Correy:", Total_of_votes_Correy)

    List_of_candidates = "Li"      
    candidate3 = "Li"
    Total_of_votes_Li = candidate.count(candidate3)
    print("Li:", Total_of_votes_Li)

    List_of_candidates = "O'Tooley"
    candidate4 = "O'Tooley"
    Total_of_votes_OTooley = candidate.count(candidate4)
    print("O'Tooley:", Total_of_votes_OTooley)

print ("___________________________________________")

#WINNER
Winner = "Khan"
print ("Winner:", Winner)
