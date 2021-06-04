#2a

shopping_cost=float(input('What is the total price of your shopping?'))
discount_applicable=str(input('Do you have a discount code? y/n'))



if shopping_cost>= 20 and discount_applicable== 'y':
    total_cost = shopping_cost*0.9
else:
    total_cost = shopping_cost

#print(f'The total cost is {total_cost}')

#2b


if shopping_cost >= 100: 
    total_cost= shopping_cost*0.95
elif shopping_cost>= 20 and discount_applicable== 'y':
    total_cost = shopping_cost*0.9
else:
    total_cost = shopping_cost

print(f'The total cost is {total_cost}')

if shopping_cost<=30:
    total_with_shipping=total_cost+5
else: 
    total_with_shipping=total_cost

print(f'The total cost is {total_with_shipping}')
