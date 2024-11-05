bill = float (input ('How much is your bill: '))
discount = bill * 0.1

if bill > 50:
    new = bill - discount
    print (f'your new bill is: {new:.2f}€')

else:
    print (f'Your total is: {bill:.2f}€')

