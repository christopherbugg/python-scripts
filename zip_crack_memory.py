#   zip_crack.py
#   python 3.5

#   Encrypted Zip-file cracker.
#   This is a memory-friendly version that doesn't load the whole file into RAM
#   Works 100% of the time, 80% of the time. Else shows false-positives.

#   Code is heavily based on implementation from Violent-Python:
#   https://github.com/igniteflow/violent-python/blob/master/pwd-crackers/zip-crack.py

#   Chris Bugg
#   Created: 11/28/16
#   Updated: 3/20/17


# The module that actually does the zip stuff
import zipfile
# The module that lets us clear the screen
import os
# The module that lets us time stuff, cool!
import time


class ZipCrack:

    def __init__(self):

        # Clear screen
        os.system('clear')

        # Print welcome
        print()
        print(">>> ZipCrack password cracker <<<")
        print(" Based on Violent-Python example")
        print()

        # Get filenames from user
        zipfilename = input('Zip file: ')
        dictionary_name = input('Dictionary file: ')

        # Clearn screen and display something nice
        os.system('clear')
        print("Searching...")
        print()

        # Define the Zip file
        zip_file = zipfile.ZipFile(zipfilename)

        # Open the Dictionary file for reading
        dictionary = open(dictionary_name, "r")

        # Seek to the start of the file
        dictionary.seek(0)

        # Initialize the line variable to the first line
        line = dictionary.readline()

        # Define some variables
        try_this = None
        password = None

        count = 0

        # A counter for total words tried
        words_tried = 0

        # Part of our timer
        start = time.time()

        # While we haven't hit the end of the file
        while not line == "":

            # Strip the newline
            try_this = line.strip('\n')

            # Try opening the file with try_this as the password
            try:
                zip_file.extractall(pwd=try_this)

                # If successful, close the zip
                zip_file.close()

                # And set password to our try
                password = try_this

                # Then break out of the for loop
                break

            # If opening fails
            except:

                # Don't worry about it, keep going
                pass

            # Grab the next line of the file
            line = dictionary.readline()

            # Increment our counters
            count += 1
            words_tried += 1

            # And print some pretty stuff for the user
            if count == 1:

                os.system('clear')

                print("Searching...")

            elif count == 5000:

                os.system('clear')

                print("Searching....")

            elif count > 10000:

                count = 0

        # Get the total time it took
        total_time = time.time() - start

        # Close the Dictionary file
        dictionary.close()

        # If password variable hasn't changed
        if password is None:

            # We didn't find anything
            print("No Luck, Sorry!")

        # Otherwise, print the found password
        else:

            print("Password Found: " + password)

        print("Ran @ " + str(round((words_tried / total_time), 4)) + "guesses per second")
        print()


ZipCrack()
