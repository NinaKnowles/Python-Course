#2a
def shopping_calculator(shopping_cost,discount_applicable):
    if shopping_cost>= 20 and discount_applicable== 'y':
        total_cost = shopping_cost*0.9
    elif shopping_cost >= 100: 
        total_cost= shopping_cost*0.95
    else:
        total_cost = shopping_cost
    print(f'The total cost is {total_cost}')

shopping_calculator(21,'y')
shopping_calculator(19,'y')
shopping_calculator(21,'n')
shopping_calculator(19,'n')

#2b
def shopping_calculator(shopping_cost,discount_applicable):
    if shopping_cost>= 20 and discount_applicable== bool(True):
        total_cost = shopping_cost*0.9
    elif shopping_cost >= 100: 
        total_cost= shopping_cost*0.95
    else:
        total_cost = shopping_cost
    print(f'The total cost is {total_cost}')

shopping_calculator(21,bool(True))
shopping_calculator(19,bool(True))
shopping_calculator(21,bool(False))
shopping_calculator(19,bool(False))