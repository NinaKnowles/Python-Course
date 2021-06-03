def my_maths_function(number1, number2, operation):
    if operation=='add':
        return(number1+number2)
    elif operation=='subtract':
        return(number1-number2)
    elif operation=='multiply':
         return(number1*number2)
    else:
        print("error")


y=my_maths_function(5, 7, 'add')
print(f"The answer is: {y}")