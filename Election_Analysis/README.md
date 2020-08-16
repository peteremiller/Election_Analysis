# Election_Analysis

##Overview of Election Audit
I was assisting a Colorado Board of Elections employee, Tom, with the ection audit of the tabulated results for a U. S. Congessional precinct. I was tasked with reporting the total votes cast, the total number of votes for each candidate, the percentage of vote for each candidate, and the winner of the election based on the popular vote. Tom's manager, Seth,  wanted to know if there was a way to automate the process, normally done in Excel, by using Python. The code that Tom and I wrote may be used not only to audit other Congressional Districts but also Senatoral District elections and local elections. 

Tom and I took into account three voting methods: mail-in ballots, punch cards, and data from direct recording electronic machines. After the votes were tabulated from all three voting  methods, Tom and I generated a vote count report to certify this particular U. S. Congessional election.


##Election Audit Results
The results of this election audit are as follows:
  1. There were 369,711 votes cast in this congressional election
  2. The percentage of votes and number of votes for each county in the precinct are:
      A. Jefferson County: 10.5% of the total vote representing 38,855 total county votes
      B. Denver County: 82.8% of the total vote representing 306,055 total county votes 
      C. Arapahoe County: 6.7% of the total vote representing 24,801 total county votes
  3. Denver County had the largest number of votes (306,055) 
  4. The three candidates in this election were: Charles Casper Stockham, Diana DeGette, 
      and Raymon Anthony Doane. They received the folowing total of votes:
      A. Stockham received 23.0% of the total votes representing 85,213 total votes
      B. DeGette received 73.8% of the total votes representing 272,892 total votes
      C. Doane recieved 3.1% of the total votes representing 11,606 total votes
   5. The winner of this congressional election is Diana DeGette. She received 73,.8% 
      of the total votes representing 272, 892 votes.


##Election Audit Summary
 In my opinion, the success of this audit provides the basis for a broader application of the script Tom and I wrote for this project. 
Using the versitility of Python code, I beleive Tom and I have demonstrated the power one has to create numerous new applications 
for performing election audits from local to national races. I have included two modifications for your onsideration:
  1. The Colorado election represnted a precint made up of three counties. In the future, rather than counties a list of states may be used in the script. For example,  
 
        county_list = []
        county_votes_dict ={}

        would become:

        state_list = []
        state_votes_dict = {}
    
      Making this change would give the auditor the ability to interate through lists of states to determine vote counts and vote percentages. 
      This would be very important tool for analyzing lager datasets, especially as one moves to the national level elections.
    
    2. The second example I would suggest is the flexibility Python provides to add an additional method for tracking the electoral college votes. 
      The script could be modified to track the elctoral college vote as well as the precint, state, reginal, and popular votes by political affiliation and 
      number of electoral votes needed to win a state.

end of analysis

