with open("sample.txt", "r") as f:  # open the text file, and keep it open until the whole file has been read. Then
    # close it
    if f.mode == "r":  # checks that file is open
        contents = f.read()  # reads the file line by line

        counter = 0  # initialises a counter for counting the number of email addresses
        for word in contents.split():  # checks every word in the file after splitting the file into individual words
            if "@softwire.com" in word:  # checks for domain name I'm searching for
                counter += 1  # counter advances if correct domain found
                word += "\n"  # formatting for printing
                print(word)
    print(counter)

# print(f.closed)
# test to check that the file has closed. Will print True if closed.
