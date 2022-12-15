import csv
import os

#files to Use
csv_path = "python-challenge/pypoll/resources/election_data.csv"
output_path = "python-challenge/pypoll/analysis/election_results.txt"

#define parameters
Candidate_n = []
Candidate_no_of_Votes = {}
Candidate_winner = ""
Count_Win = 0
Total_Votes = 0

#Read CSV 
with open(csv_path) as election_data:
    csvreader = csv.reader(election_data)

    # read the header row
    csv_header = next(csvreader)

    for row in csvreader:

        # Calculate Totals
        Total_Votes = Total_Votes + 1


        id_string = row[0]
        value_string = row[2]

        #get candidate name
        Candidate_names = value_string

        #if candidate not matching
        if Candidate_names not in Candidate_n:
            Candidate_n.append(Candidate_names)

            #add to the voter count
            Candidate_no_of_Votes[Candidate_names] = 0

        #add vote to candidate
        Candidate_no_of_Votes[Candidate_names] = Candidate_no_of_Votes[Candidate_names] + 1
    
#print results & write to txt file
with open(output_path, "w") as txt_file:

    #print final results
    election_results = (
        f"Election Results\n"
        f"--------------------\n"
        f"Total Votes : {Total_Votes}\n"
        f"--------------------\n"
    )
        
    print(election_results)
           
    #write election result
    txt_file.write(election_results)
    
    for candidate in Candidate_no_of_Votes:

        E_votes = Candidate_no_of_Votes.get(candidate)
        E_vote_percentage = float(E_votes) / float(Total_Votes) * 100

        #Votes count & candidate
        if(E_votes > Count_Win):
            Count_Win = E_votes
            Candidate_winner = candidate
        
        #print each candidate voter count & percentage
        Voter_Output = f"{candidate}: {E_vote_percentage:.2f}% ({E_votes})\n"
        print(Voter_Output)

        #write voter count & each percentage
        txt_file.write(Voter_Output)

    #print the winner
    Election_Winners_Summary = (
        f"-------------------\n"
        f"Winner: {Candidate_winner}\n"
        f"-------------------\n"
    )
    print(Election_Winners_Summary)
           
    #write to the txt file
    txt_file.write(Election_Winners_Summary)










        





