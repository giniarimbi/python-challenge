import csv
import os
import sys
from operator import itemgetter


#variable to be used in the exercise
total_vote=0

name_candidate=[]
candidate_votes=[]
total_candidate_votes={}
sortedcandidate=[]

top_1=0
top_2=0

winner_votes=0

#path for source data (csvpath) and text output data (outputpath)
outputpath = os.path.join('.', 'output_election.txt')

csvpath=os.path.join('.','houston_election_data.csv')
with open('houston_election_data.csv', encoding="UTF-8") as f:
    reader = csv.reader(f, delimiter=',')
#     csv_header=next(reader)

    for row in reader:
        #calculate total_vote
        total_vote = total_vote + 1
  
        #calculate name of candidates & votes per candidate 
        if row[0] not in total_candidate_votes.keys():
                total_candidate_votes[row[0]]=1

        else:
                total_candidate_votes[row[0]]+=1


         #formula to sort from highest to lowest vote
        sortedcandidate = sorted(total_candidate_votes.items(), key=itemgetter(1), reverse=True)


        # name_candidate=total_candidate_votes.keys
        # candidate_votes=total_candidate_votes.value

        # print(name_candidate)

        # percentage=(total_candidate_votes["Voter ID"])/total_vote
        # percentage.append(row[2])

        #Find 1st and 2nd Winner
        # for name,value in total_candidate_votes.items():
        #     if value>top_1:
        #         top_1=value
        #         name_1=name
        #     elif value>top_2 and value<top_1:
        #         top_2=value
        #         name_2=name
        # print("{}{}".format(name,value))
        
     

#print total_vote
print("Total Votes: " + str(total_vote))

# print name and total vote candidate
print(f"{sortedcandidate}") 

#print name candidate, percentage win, total candidate

# #print 1st and 2nd winner




# #output text
with open(outputpath, "w") as txt_file:
    
        txt_file.write("Houston Mayoral Election Results \n")
        txt_file.write("Total Votes " + str(total_vote) + "\n")
        txt_file.write("-------------------------\n")
#txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
#txt_file.write(str(winner))
        txt_file.write(str(sortedcandidate))
        txt_file.write("\n")
        txt_file.write("-------------------------\n")
        txt_file.write("1st Advancing candidate: " )
        txt_file.write("\n")
        txt_file.write("2nd Advancing candidate: " )
        txt_file.write("\n")
        txt_file.write("-------------------------\n")
# '''