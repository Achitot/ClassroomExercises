#
number = int(input("Enter a number: "))
while number >= 0:
    print(number)
    number -= 1
#
for i in range (1,11):
    print (i)

#
total = 0
for i in range (1,6):
    total += i
print("Sum: ", total)

#
text = input("Enter a string: ")
for char in text:
    print(char)

#
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#
for i in range(0, 51,):
    if i%2 != 0:
        print(i)

#
numbers = [12, 4, 56, 17, 8]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print("Minimum value:", minimum)  

#
import random
target = random.randint(1,50)
guess = None
while guess != target:
    guess = int(input("Guess a number between 1 and 50: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
print("Correct!")