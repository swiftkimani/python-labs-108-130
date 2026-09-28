# Lab 130 - Debugging Hello World
# All five bugs fixed


def get_greeting(name):
    greeting = "Hello, " + name + "!"
    return greeting                       # fix 1 - return the greeting


def repeat_greeting(greeting, times):
    messages = []
    for i in range(times):
        print(greeting)
        messages.append(greeting)
    return messages                       # fix 2 - return the list


def main():
    name = "World"

    greeting = get_greeting(name)
    print(greeting)

    length = len(name)
    print("The name has " + str(length) + " characters")
    # fix 3 - str() converts the number so it can be joined

    messages = repeat_greeting(greeting, 3)
    print("Printed " + str(len(messages)) + " messages")
    # fix 4 - messages is a real list now, so len() works

    names = ["World", "Python", "AWS"]
    for name in names:
        print(get_greeting(name))
    # fix 5 - loop through the list directly, so there is no index to get wrong


main()
