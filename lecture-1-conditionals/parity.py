# x = int(input("Enter a number: "))
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(_):
    return _ % 2 == 0
main()