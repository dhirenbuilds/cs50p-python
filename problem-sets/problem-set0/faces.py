def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    user_input = input("Say something: ")
    print(convert(user_input))


main()
