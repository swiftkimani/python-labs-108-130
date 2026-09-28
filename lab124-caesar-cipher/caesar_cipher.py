# Lab 124 - Use Functions to Implement a Caesar Cipher
# AWS re/Start - Python Programming

# A Caesar cipher shifts every letter forward by a fixed number of places
# and wraps around at the end of the alphabet. Shift 3: A becomes D, X becomes A.


def shift_letter(letter, shift):
    """Shift one letter by the given number of places."""
    if letter.islower():
        start = ord("a")
    elif letter.isupper():
        start = ord("A")
    else:
        # Not a letter, so leave it as it is
        return letter

    # ord() gives the number for the letter, % wraps it round,
    # chr() turns the number back into a letter
    position = (ord(letter) - start + shift) % 26
    return chr(start + position)


def encrypt(text, shift):
    """Encrypt the text by shifting every letter forward."""
    result = ""
    for letter in text:
        result = result + shift_letter(letter, shift)
    return result


def decrypt(text, shift):
    """Decrypt the text by shifting every letter backward."""
    return encrypt(text, -shift)


def brute_force(text):
    """Try every possible shift and print the result."""
    for shift in range(1, 26):
        print(f"Shift {shift:2}: {decrypt(text, shift)}")


# ----- TESTING THE FUNCTIONS -----
# Only runs when this file is run directly, not when it is imported
if __name__ == "__main__":
    message = "Hello World"
    shift = 3

    print("Original: ", message)

    encrypted = encrypt(message, shift)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, shift)
    print("Decrypted:", decrypted)

    if decrypted == message:
        print("\nThe message was recovered correctly")
    else:
        print("\nSomething went wrong")

    # Try different shifts
    print("\nTrying different shifts")
    for s in [1, 5, 13, 25]:
        print(f"Shift {s:2}: {encrypt(message, s)}")

    # Letters wrap around at the end of the alphabet
    print("\nWrapping around")
    print("encrypt('xyz', 3) =", encrypt("xyz", 3))
    print("encrypt('XYZ', 3) =", encrypt("XYZ", 3))

    # Numbers and punctuation are not changed
    print("\nNon-letters stay the same")
    mixed = "AWS re/Start 2026!"
    print("Original: ", mixed)
    print("Encrypted:", encrypt(mixed, 5))
    print("Decrypted:", decrypt(encrypt(mixed, 5), 5))

    # Brute force - when you do not know the shift
    print("\nBrute forcing a secret message")
    secret = encrypt("Meet me at noon", 7)
    print("Ciphertext:", secret)
    print()
    brute_force(secret)
