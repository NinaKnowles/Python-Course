
#1a
shirt_price= float(input('What is the price of the shirt?'))

within_budget = shirt_price <= 25.00
print(f'shirt is available within budget: {within_budget}')

#1b
shirt_colour= str(input('What is the colour of the shirt?'))

correct_colour= shirt_colour == 'yellow'
print(f'shirt is available within budget and correct colour: {within_budget and (correct_colour)}')

