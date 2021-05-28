#The data we need to retrive.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the elections based on popular vote

import os
import csv
import random
import numpy


file_to_load = os.path.join('..',"Resources","election_results.csv")

# Open the election results and read the
election_data = open(file_to_load,'r')

print(election_data)



