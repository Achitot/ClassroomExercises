balance = float (input ('Account Balance: '))
withdraw = float (input ('How much you want to withdraw? '))

if withdraw <= balance:
    remaining = balance - withdraw
    if remaining > 1000:
        print ('You are a VIP')
    if remaining < 100:
        print ('Your balance is getting low.')

else:
    print ("You are not allowed to withdraw")