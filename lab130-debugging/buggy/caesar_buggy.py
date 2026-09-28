# Lab 130 - Debugging the Caesar Cipher
# This version has bugs in it. Most of them do not crash the program,
# they just give the wrong answer, which makes them harder to find.


def shift_letter(letter, shift):
    if letter.islower():
        start = ord("a")
    elif letter.isupper():
        start = ord("a")
        # bug 1 - should be ord("A") for capital letters
    else:
        return letter

    position = ord(letter) - start + shift
    # bug 2 - there is no % 26, so letters run past the end of the alphabet
    return chr(start + position)


def encrypt(text, shift):
    result = ""
    for letter in text:
        result = shift_letter(letter, shift)
        # bug 3 - this should be result = result + ...
    return result


def decrypt(text, shift):
    return encrypt(text, shift)
    # bug 4 - should be -shift, otherwise it encrypts a second time


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
