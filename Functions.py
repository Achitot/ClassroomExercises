#
def greet_user(name):
    """Greets the user with their name."""
    return f"Hello, {name}! Welcome to Python programming."
print (greet_user("Usman"))

#
def add_numbers(num1, num2, num3):
    """Adds two numbers and returns the result."""
    return num1 + num2 + num3

print (add_numbers(3,5,9))

#
def check_even_odd(number):
    """Check if a number is even or odd"""
    return "Even" if number % 2 == 0 else "Odd"

print(check_even_odd(7))
print(check_even_odd(8))

#
def find_largest(num1,num2,num3):
    """Finds and returns the largest of three numbers"""
    return max (num1,num2,num3)

print (find_largest(10,20,15))

#
def reverse_string(text):
    """Reverses the input string"""
    return text[::-1]

print (reverse_string("Python"))

#
def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))


