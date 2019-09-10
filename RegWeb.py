import re  # import the library for regular expressions
import requests  # importing library  URL requests
from bs4 import BeautifulSoup  # installing package that makes an htt request

url = "https://www.pristonmill.co.uk/contact-us/"
response = requests.get(url)
website_string = str(BeautifulSoup(response.text, "html.parser"))

email_address = re.findall(r"(\S+@(\w+)\.\w+\.?\S*\b)", website_string)  # use a regular expression to find all
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
        email_address_dict[email[0]] += 1

    else:
        email_address_dict[email[0]] = 1

    if email_address_dict[email[0]] > 1:
        email_address_dict[email[0]] -= 1  # removes all duplicated email addresses from counts
        email_domain_dict[email[1]] -= 1

sort_email_domain = sorted(email_domain_dict.items(), key=lambda x: x[1], reverse = True)  # sorts the list
# of domains from most to least popular (switches the key from x[0] (the key) to x[1] (the value).)

top = int(input("Please enter the minimum frequency you require:"))
print("Domain", " Count")
for domain in sort_email_domain:
    if domain[1] < top:  # doesn't print any domains where the frequency is less than the user requested.
        break
    else:
        print(str(domain[0]), ":", str(domain[1]))  # printing formatted
