#November 26 2024
list_of_subjects = {
    "Math": 80, "Science":81, "PE":90, "English":89
}

list_of_subjects["PE"] = 98
list_of_subjects["Psychology"] = 50
del list_of_subjects["PE"]
print(list_of_subjects)

#November 27 2024
#exercise 1
student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}

print(f"Name: {student['Name']}")
print(f"Major: {student['Major']}")

#exercise 2
student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}
student["GPA"] = 3.8
student["Age"] = 25

print(student)

#exercise 3
student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}
student["GPA"] = 3.8
student["Age"] = 25

for key, value in student.items():
    print(f'{key}: {value}')

#exercise 4
student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}
student["GPA"] = 3.8
student["Age"] = 25

def check_key(dictionary, key):
    if key in dictionary:
        return "Key exist"
    else:
        return "Key does not exist"
    
print(check_key(student,"Name"))
print(check_key(student,"Hobbies"))

#exercercise 5
fruits = ["apple","banana","apple","orange","banana","apple"]
word_count = {}

for word in fruits:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

#exercise 6
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)

#exercise 7
student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}
student.pop("Age", None)

print(student)

#exercise 8
classroom = {
    "Student1": {"Name": "John", "Age": 20},
    "Student2": {"Name": "Emma", "Age": 22}
}

print(f"Student 2 Name: {classroom["Student2"]["Name"]}")
print(f"Student 1 Age: {classroom["Student1"]["Age"]}")
