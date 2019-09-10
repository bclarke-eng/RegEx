import re  # import the library for regular expressions

with open("sample.txt", "r") as f:  # open the text file, and keep it open until the whole file has been read. Then
    # close it
    if f.mode == "r":  # checks that file is open
        contents = f.read()  # reads the file line by line

        email_address = re.findall(r"(\S+@(\w+)\.\w+\.?\S*\b)", contents)  # use a regular expression to find all
        # emails and domains and store them in tuples.

        email_address_dict = {}  # creates empty dictionaries
        email_domain_dict = {}

        for email in email_address:

            if email[1] in email_domain_dict:  # if the [1] value of the email address tuple (the domain) has already
                # been identified, the counter for that domain name increases
                email_domain_dict[email[1]] += 1
            else:
                email_domain_dict[email[1]] = 1  # otherwise, if there is only one email with that domain, that is
                # entered

            if email[0] in email_address_dict:  # if the [0] value of the email address tuple (the full email) has
                # already been identified, the counter for that email address increases
                email_address_dict[email[0]] += 1  # this essentially checks for duplicate addresses

            else:
                email_address_dict[email[0]] = 1

        for i, v in email_domain_dict.items():
            print(i, v)  # prints the domain names and how many email addresses are in that domain in a nice format
