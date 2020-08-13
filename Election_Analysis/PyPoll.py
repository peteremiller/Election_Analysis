#Examine the data for structure, content and mistakes
#Visualize the end result: what does Tom/Seth need from me?
#Determine the data I need to retrieve to accomplish the overall goal
#Determine a list of all candidates 
#How many candidates received votes
#Determine the num of votes each candidate received
#Determine the percentage of votes each candidate received
#Determine the total num of votes received by all candidates
#Determine who won the election by popular vote
#
import csv
import os
#Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read and print the header row.
    headers = next(file_reader)
    print(headers)
        


