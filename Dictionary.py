#Dictionary
student = {
    "name" : "Alice",
    "age" : 20,
    "courses" : ["Math", "Physics"]
}

print (student)

#Dictionary Modified
book = {
    'Title' : 'Percy Jackson',
    'Price' : 65,
    'Quantity' : 1
}

print (book)

#Student Information Dictionary
student_info = {
    'name':'Bob',
    'age':21,
    'major':'computer science'
}

student_info2 = dict(name='emma',age=22,major='biology')

print (student_info)
print (student_info2)

#Accesing Dictionary Elements
student = {
    "name" : "charlie",
    "age" : 19,
    "courses" : "Physics",
} 
print(student["name"])
print(student.get("GPA", "Not available"))

#Modifying Dictionary
student = {
    "name" : "dave",
    "age" : 20,
    "courses" : "chemistry",
} 

student["GPA"] = 3.8
student["age"] = 21
student.pop("courses")
print(student)