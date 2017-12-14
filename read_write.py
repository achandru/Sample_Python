import itertools
from datetime import datetime
from datetime import timedelta



CurDate= datetime.now()
OutFile = open('abcd' +'.xlsx', 'w')

file = open ("apr21_30.csv", "r")
contect = file.readlines()

for line in itertools.islice(contect, 19,52):
   for Offer in line:
     OutFile.write(Offer+'\n')
