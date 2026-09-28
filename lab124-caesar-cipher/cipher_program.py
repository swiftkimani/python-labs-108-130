# Lab 124 - Use Functions to Implement a Caesar Cipher
# Interactive version

from caesar_cipher import encrypt, decrypt, brute_force

print("Caesar Cipher")
print("1 - Encrypt a message")
print("2 - Decrypt a message")
print("3 - Brute force a message")

choice = input("\nChoose an option: ")

if choice == "1":
    message = input("Enter the message: ")
    shift = int(input("Enter the shift: "))
    print("\nEncrypted:", encrypt(message, shift))

elif choice == "2":
    message = input("Enter the message: ")
    shift = int(input("Enter the shift: "))
    print("\nDecrypted:", decrypt(message, shift))

elif choice == "3":
    message = input("Enter the message: ")
    print()
    brute_force(message)

else:
    print("That is not a valid option")
