import requests


inventory_response = {
 "product_code":"le34",
 "product_name":"Magic Bulb - Large",
 "fitting_type": "e14",
 "stock": 2,
 "unit_dimensions_cm":
 {
 "width": 20,
 "height": 40,
 "depth": 20
 },
 "upcoming_deliveries": [
 {
 "date": "01/02/2022",
 "quantity": 225
 },
 {
 "date": "01/03/2022",
 "quantity": 245
 }
 ],
 "unit_price":24.32,
 "unit_currency":"EUR"
 }

#1a

print(inventory_response['product_name'])

#1b)

print(inventory_response['upcoming_deliveries'][0]['quantity'])
a=(inventory_response['upcoming_deliveries'][0]['quantity'])
b=(inventory_response['upcoming_deliveries'][1]['quantity'])
sum1=a+b
print(a)
print(b)
print(sum1)

sum=0
for item in inventory_response['upcoming_deliveries']:
    sum=sum+item['quantity']
print(sum)


#1c)

#print(inventory_response['upcoming_deliveries'][0]['date'])

#1d)
#print(inventory_response['unit_dimensions_cm']['width'])

#1e)
#print(inventory_response['unit_price'])
#print(inventory_response['unit_currency'])



