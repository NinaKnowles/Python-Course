#1a 

#for number in range (11):
   # if number%3==0:
        #continue
    #else:
       # print(number)


#1b

#def print_nums(a):
   # for number in range (a):
       # if number%3==0:
            #continue
        #else:
           # print(number)

#print_nums(11)

#1c

def print_nums():
    max_number=int(input('What is the max number?'))
    for number in range (max_number):
        if number%3==0:
            continue
        else:
            print(number)

print_nums()

