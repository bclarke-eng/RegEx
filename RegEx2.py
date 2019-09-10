import re  # import the library for regular expressions

with open("sample.txt", "r") as f:  # open the text file, and keep it open until the whole file has been read. Then
    # close it
    if f.mode == "r":  # checks that file is open
        contents = f.read()  # reads the file line by line

        emails = (re.findall(r"\S+@softwire\.com\b", contents))  # use a regular expression for find all emails with
        # the softwire.com domain
        counter = len(emails)  # the list of all emails that meet the criteria is stored in a list, so the number of
        # emails is the length of the list

        print(emails)  # prints the list of all softwire emails
        print(counter)  # prints the number of softwire emails found
