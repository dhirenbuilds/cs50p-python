def main():
    name = input("What's your name: ").strip().title()
    print(f"Hello, {name}!")

def hello(to = "World"):
    print("Hello,", to)

main()
