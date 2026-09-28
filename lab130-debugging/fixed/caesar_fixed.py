# Lab 130 - Debugging the Caesar Cipher
# All four bugs fixed


def shift_letter(letter, shift):
    if letter.islower():
        start = ord("a")
    elif letter.isupper():
        start = ord("A")                  # fix 1 - capitals start at "A"
    else:
        return letter

    position = (ord(letter) - start + shift) % 26
    # fix 2 - the % 26 wraps z round to a
    return chr(start + position)


def encrypt(text, shift):
    result = ""
    for letter in text:
        result = result + shift_letter(letter, shift)
        # fix 3 - build the string up instead of replacing it
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)          # fix 4 - shift backwards


message = "Hello World"
shift = 3

encrypted = encrypt(message, shift)
print("Original: ", message)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)

if decrypted == message:
    print("The message was recovered")
else:
    print("The message was NOT recovered")

# Checking the bugs are really fixed
print("\nChecking the fixes")
print("Capitals:", encrypt("ABC", 3), "- should be DEF")
print("Wrapping:", encrypt("xyz", 3), "- should be abc")
print("Full string:", encrypt("Hello World", 3), "- should be Khoor Zruog")
print("Round trip:", decrypt(encrypt("Hello World", 3), 3), "- should be Hello World")
