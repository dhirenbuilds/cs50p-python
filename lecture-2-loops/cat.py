# i = 3
# while i < 3:
#     print("Meow")
#     i += 1

# while i != 0:
#     print("Meow")
#     i -= 1

# print("meow\n" * 3, end="")

# for _ in range(3):
#     print("meow")

n = int(input("Enter a number: "))

while n < 0:
    print("Please enter a non-negative number.")
    n = int(input("Enter a number: "))