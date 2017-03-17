#   better_rot13.py
#   python 3.5

#   This is a tool to perform ROT-13 "encryption".
#   It can handle only lower-case letters for now.

#   Chris Bugg
#   3/16/17

# Imports
import os


# ROT13 Class
class ROT13:

    # Constructor
    def __init__(self):

        while True:

            # Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-- ROT-13 --")
            print()
            print("1 - Encrypt Text")
            print("2 - Decrypt Text")
            print("3 - Exit")
            print()

            choice = input("Choice: ")

            # Input sanitization
            good_choices = {"1", "2", "3"}

            while choice not in good_choices:

                print("Input Error!")

                choice = input("Try Again: ")

            # Encrypt Text
            if choice == "1":

                self.encrypt()

            # Decrypt Text
            elif choice == "2":

                self.decrypt()

            # Exit
            else:

                exit()

    # Encrypt Text
    def encrypt(self):

        plainText = input("Enter text to encrypt: ").replace(" ", "").lower()

        # Convert string to list of chars
        textList = list(plainText)

        # Create a new string to hold the ciphertext
        ciphertext = ""

        # For each character in the string
        for char in textList:

            # Convert char to int (97 - 122) and add 13
            char = ord(char) + 13

            # If overflows 122, start from 97
            if int(char) > 122:

                char -= 26

            # Convert back to char
            ciphertext += chr(char)

        print("Ciphertext: " + ciphertext)
        input("Enter to continue")

    # Decrypt Text
    def decrypt(self):

        plainText = input("Enter text to decrypt: ").replace(" ", "").lower()

        # Convert string to list of chars
        textList = list(plainText)

        # Create a new string to hold the ciphertext
        plaintext = ""

        # For each character in the string
        for char in textList:

            # Convert char to int (97 - 122) and add 13
            char = ord(char) - 13

            # If overflows 122, start from 97
            if int(char) < 97:
                char += 26

            # Convert back to char
            plaintext += chr(char)

        print("Plaintext: " + plaintext)
        input("Enter to continue")

ROT13()
