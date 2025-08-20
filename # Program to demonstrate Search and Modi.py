# Program to demonstrate Search and Modification operations

# Initial list
students = ["A", "B", "C", "D", "E"]

print("Original Student List:", students)

# Search Operation
name = input("Enter the name to search: ")

if name in students:
    print(f"{name} is found at position {students.index(name)}")
    
    # Modification Operation
    new_name = input(f"Enter new name to replace {name}: ")
    students[students.index(name)] = new_name
    print("List after modification:", students)
else:
    print(f"{name} not found in the list.")