# Election_Analysis  

## Overview of Election Audit  

The main objective of this audit is to determine the total number of votes cast in the election, track votes casted for each candidate and determine the election winner. the secondary objective is to determine number of votes cast per county as a total and percentage of total votes.

## Elections-Audit Results  

Using python we read and analysis the elections data from the csv file provided. Based on this information and the help of our code we were able to determine the following elections results:


1. The total number of votes were 369,711  
2. The percentage and number of votes per county:  
    Jefferson: 10.5% (38,855)  
    Denver: 82.8% (306,055)  
    Arapahoe: 6.7% (24,801)  
  
3. The county with the largest turnout was Denver.  
4. The percentage and number of votes per candidate:  
    Charles Casper Stockham: 23.0% (85,213)  
    Diana DeGette: 73.8% (272,892)  
    Raymon Anthony Doane: 3.1% (11,606)  

5. Base the these results the election winner is:  
    Diana DeGette: 73.8% (272,892)  
    
   
 As mentions before these results were gather using python to extract the information for the source file, and the results were saved in the below text file:


[election_analysys.txt](https://github.com/calvogeorge/Election_Analysis/blob/ef223425156f801d7a387a2ae87fbb958bc1440a/Analysis/election_analysis.txt)

## Election Audit Summary  

The code writing for this analysis is a great tool to further analyze any elections results in a reliable and quick manner. The code can read information for any number of candidates that received votes, any number of counties that participated in the elections and save it in clear easy to read text file summarizing the results with any elections.
With some minor modifications the code can be adjusted to provide even deeper levels of information, as *votes per candidate and county*, to provide information as how a particular candidate performed at a more local level.

As different needs for the Elections Commission arises the code can be adjusted to provide the information needed, such as turnout as percentage of registered votes, among other possible analysis. 

