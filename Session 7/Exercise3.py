#3a

import csv

with open('c:/Users/CAMNK3/Python/Week 7/scoreboard.csv', 'r') as file:

    csvreader = csv.reader(file)

    for row in csvreader:

        print(row)

 

#3b 

 

#with open('c:/Users/CAMNK3/Python/Week 7/scoreboard.csv', 'r') as file:

    #csvreader = csv.reader(file)

   # for row in csvreader:

      #  print(f'{row[0]} had a high score of {row[1]}')

 

#3c & Extension

with open('c:/Users/CAMNK3/Python/Week 7/scoreboard.csv', 'a') as file:

    csvwriter = csv.writer(file)

    csvwriter.writerow(['Steven','20'])

 

with open('c:/Users/CAMNK3/Python/Week 7/scoreboard.csv', 'a') as file:

    csvwriter = csv.writer(file)

    csvwriter.writerows([['Nina','100'],['Chris','99']])

 

with open('c:/Users/CAMNK3/Python/Week 7/scoreboard.csv', 'r') as file:

    csvreader = csv.reader(file)

    for row in csvreader:

        if row != []:

            print(f'{row[0]} had a high score of {row[1]}')