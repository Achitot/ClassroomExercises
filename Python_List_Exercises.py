#exercise 1
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits)

#excercise 2
num1 = [10, 20, 30, 40, 50]
print ('First element: ', num1 [0])
print ('Last elemet: ', num1 [-1])

#exercise 3
animals = ['cat', 'dog', 'bird']
animals[2] = 'snake'
print (animals)

#exercise 4
colors = []
colors.append('red')
colors.append('green')
colors.append('blue')
colors.remove('green')
print (colors)

#exercise 5
name = ['alice', 'bob', 'charie', 'diana']
print('Length of the list:', len(name))

#exercise 6
num2 = [4, 7, 1, 8, 5]
total = sum(num2)
print ('Sum of elements: ', total)

#exercise 7
age = [23, 45, 18, 34, 60]
print ('Maximum age:', max(age))
print ('Mininmum age', min(age))

#exercise 8
scores = [88, 56, 92, 78, 61]
scores.sort()
print ('Score lists:', scores)

#exercise 9
num3 = [1, 3, 5, 7, 9]
if 5 in num3:
    print('Found')
else:
    print('Not Foun')

#exercise 10
items = [1, 2, 3, 4, 4, 4, 5]
counts = items.count(4)
print ('Count of 4:', counts)

#execerise 11
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
list1.extend (list2)
print (list1)