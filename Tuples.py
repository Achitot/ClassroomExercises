#Basic Tuple
fruits = ('apple','banana','cherry')
print (fruits)

#Accesing Elements
print(fruits[1])
print(fruits[-1])

#Unpacking Tuples
colors = ('red','green','blue')
color1, color2, color3 = colors
print(color1)
print(color2)
print(color3)

#Tuple Concatenation
numbers1 = (1, 2, 3)
number2 = (4, 5, 6)
numbers_combined = numbers1 + number2
print (numbers_combined)

#Tuple Slicing
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(alphabet[:3])
print(alphabet[-3:])
print(alphabet[::2])

#Tuple Methods
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
print(numbers.count(4))
print(numbers.index(2))

#Nested Tuples
nested = (1, 2, (3, 4), 5)
print(nested[2][1])

#Tuple Membership Testing
colors = ('red', 'green', 'blue')
print('yellow' in colors)
print('blue' in colors)
