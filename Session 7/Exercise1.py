#1a

 

with open('c:/Users/CAMNK3/Python/Week 7/groceries.txt', 'r') as file:

 print(file.read())

 

#1b

with open('c:/Users/CAMNK3/Python/Week 7/groceries.txt', 'r') as file:

    print(file.readline(4))

 

#1c

 

with open('c:/Users/CAMNK3/Python/Week 7/groceries.txt', 'r') as file:

    a=(file.readlines())

    for string in a:

        print(string.capitalize())

 

#Extension

 

i=0

with open('c:/Users/CAMNK3/Python/Week 7/groceries.txt', 'r') as file:

    a=(file.readlines())

    for string in a:

        i=i+1

        print(f'{i}. {string.capitalize()}')