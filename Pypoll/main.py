import os
import csv


#Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#Open csv file
with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(election_data)
    

    #Set Variables
    total_votes = []
    election_data_list = []
    candiates_dic = {}
    candiate = []
    voters_count = []
    candiate_name_vote_list = []
    most_votes = 0
    

    


    for row in election_data:
        #Sum of votes
        total_votes.append(election_data)

        #Setting candiatelist
        candiate = row[2]
        if candiate in (candiates_dic):
            candiates_dic[candiate] += 1
        else:
            candiates_dic[candiate] = 1
    #Make dictionary into list
    for key, value in candiates_dic.items():
        candiate_name_vote_list += key,value
        winner = max(candiates_dic, key = candiates_dic.get)
        
#The percentage of votes each candiate won
candiate_1_votes = (candiate_name_vote_list[1])/(len(total_votes))*100
candiate_2_votes = (candiate_name_vote_list[3])/(len(total_votes))*100
candiate_3_votes = (candiate_name_vote_list[5])/(len(total_votes))*100




#Print results
print(f'''Election Results
------------------------- 
Total Votes: {len(total_votes)} 
------------------------- 
{candiate_name_vote_list[0]}: {round((candiate_1_votes), 3)}% ({candiate_name_vote_list[1]})
{candiate_name_vote_list[2]}: {round((candiate_2_votes), 3)}% ({candiate_name_vote_list[3]})
{candiate_name_vote_list[4]}: {round((candiate_3_votes), 3)}% ({candiate_name_vote_list[5]})
-------------------------
Winner: {winner}
-------------------------
            ''')

#save results to text file
with open("PyPoll_Election_Results.txt", "w") as f:
    f.write(f'''Election Results
------------------------- 
Total Votes: {len(total_votes)} 
------------------------- 
{candiate_name_vote_list[0]}: {round((candiate_1_votes), 3)}% ({candiate_name_vote_list[1]})
{candiate_name_vote_list[2]}: {round((candiate_2_votes), 3)}% ({candiate_name_vote_list[3]})
{candiate_name_vote_list[4]}: {round((candiate_3_votes), 3)}% ({candiate_name_vote_list[5]})
-------------------------
Winner: {winner}
-------------------------
            ''')