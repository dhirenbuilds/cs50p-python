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

# n = int(input("Enter a number: "))

# while n < 0:
#     print("Please enter a non-negative number.")
#     n = int(input("Enter a number: "))

# while True:
#     n = int(input("Enter a number: "))
    # if n < 0:
    #     continue
    # else:
    #     break
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)


def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n
        else:
            continue


main()