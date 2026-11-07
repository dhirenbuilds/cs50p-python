# Ask user for their name and Remove white space from strings
name = input("What's your name: ").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Say hello to the user
print(f"Hello, {first}!")
print(first)

print("Hello, \"Friends\"!")