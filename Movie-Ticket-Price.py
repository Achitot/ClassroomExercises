age = int (input ('Enter you age: '))

if age <= 12:
    print ('5€')

elif age > 12 and age <= 17:
    print ('7€')

elif age >17 and age <= 64:
    print ('10€')

else:
    print ('6€')