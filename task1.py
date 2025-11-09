students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

name = input("Enter the student's name: ")

if name in students:
    print(f"\n{name}'s marks: {students[name]}")
else:
    print("\nStudent not found.")
