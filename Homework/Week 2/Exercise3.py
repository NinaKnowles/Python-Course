
def adding_function():
    sum_=0
    while True:
        number = input('Enter a number to add, hit enter if you don''t want to add any more numbers')
        print(f">{number}<")
        if number == '':
            print(f'Total={sum_}')
            break
        else:
            sum_+= int(number)

adding_function()