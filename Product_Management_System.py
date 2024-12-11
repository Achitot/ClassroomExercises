product = {'A' : ("A1",10),
           'B' : ("A2",10),
           'C': ("A3",10),
           'D' : ("A4",10),
           'E' : ("A5",10),
           'F' : ("A6",10),
           'G' : ("A7",10),
           'H' : ("A8",10),
           'I' : ("A9",10),
           'J' : ("A10",10),
           'K' : ("A11",10),
           'L' : ("A12",10),
           'M' : ("A13",10),
           'N' : ("A14",10),
           'O' : ("A15",10)
           }

def display():
    for code, (name, price) in product.items():
        print(f"{code}: {name} - {price:.2f}")

def choice():
    code = (input("Enter your choice: ")).capitalize()  # Corrected here by adding parentheses
    if code in product:
        return code
    else:
        print("Invalid choice")
        return None
    
display()
selected_choice = None
while selected_choice is None:
    selected_choice = choice()

item_name, item_price = product[selected_choice]  # Corrected the dictionary lookup here
print(f"\nYour selected: {selected_choice} - {item_name} {item_price:.2f}")
