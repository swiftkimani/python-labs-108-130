# Lab 130 - Debugging Hello World
# This version has bugs in it. Find them and fix them.


def get_greeting(name):
    greeting = "Hello, " + name + "!"
    # bug 1 - the greeting is never returned


def repeat_greeting(greeting, times):
    for i in range(times):
        print(greeting)
    # bug 2 - the list of messages is never returned


def main():
    name = "World"

    greeting = get_greeting(name)
    print(greeting)

    length = len(name)
    print("The name has " + length + " characters")
    # bug 3 - cannot join a string and a number with +

    messages = repeat_greeting(greeting, 3)
    print("Printed " + str(len(messages)) + " messages")
    # bug 4 - messages is None so len() fails

    names = ["World", "Python", "AWS"]
    for i in range(len(names) + 1):
        print(get_greeting(names[i]))
    # bug 5 - this goes one past the end of the list


main()
