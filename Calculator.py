# This function performs basic arithmetic operations: addition, subtraction, multiplication, and division.
def calculator(first_number, second_number, choice):
    # Check if the user selected 'Add' operation and return the sum of the numbers
    if choice == "Add":
        return first_number + second_number
    # Check if the user selected 'Subtract' operation and return the difference of the numbers
    elif choice == "Subract":  # Note: There is a typo in 'Subract' (should be 'Subtract')
        return first_number - second_number
    # Check if the user selected 'Multiply' operation and return the product of the numbers
    elif choice == "Multiply":
        return first_number * second_number
    # Check if the user selected 'Divide' operation and return the quotient of the numbers
    elif choice == "Divide":
        return first_number / second_number
    # If the choice doesn't match any valid operation, return an error message
    else:
        return ("Invalid Choice")
    
# Prompt user for input: first number for the calculation
first_number = int(input("Enter 1st number: "))
# Prompt user for input: second number for the calculation
second_number = int(input("Enter 2nd number: "))
# Prompt user to select the operation and capitalize the input
choice = input("Enter your choice (Add, Subtract, Multiply, Divide): ").capitalize()

# Call the calculator function and store the result
result = calculator(first_number, second_number, choice)

# Output the result of the operation
print("Result: ", result)
