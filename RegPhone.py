import re  # import the library for regular expressions
import requests  # importing library  URL requests
from bs4 import BeautifulSoup  # installing package that makes an htt request

url = "https://cosyclub.co.uk/location/bath/"
response = requests.get(url)
website_string = str(BeautifulSoup(response.text, "html.parser"))

phone_number = re.findall(r"(\(?0\d{4}\)?\s*\d{6}\s*)|(\s*\(?0\d{3}\)?\s*\d{3}\s*\d{4}\s*)", website_string)
# use a regular expression to find all phones and domains and store them in tuples.

phone_number_dict = {}  # creates empty dictionary

for phone in phone_number:

    if phone[0] in phone_number_dict:  # if the [0] value of the phone number tuple (the full email) has
        # already been identified, the counter for that phone number increases
        phone_number_dict[phone[0]] += 1

    else:
        phone_number_dict[phone[0]] = 1

    if phone_number_dict[phone[0]] > 1:
        phone_number_dict[phone[0]] -= 1  # removes all duplicated phone numbers from counts

sort_phone_numbers = sorted(phone_number_dict.items(), key=lambda x: x[1], reverse=True)  # sorts the list
# of domains from most to least popular (switches the key from x[0] (the key) to x[1] (the value).)

low = int(input("Please enter the minimum frequency you require:"))
for number in sort_phone_numbers:
    if number[1] < low:  # doesn't print any domains where the frequency is less than the user requested.
        break
    else:
        print("Number:", str(number[0]), "\n Frequency:", str(number[1]))  # printing formatting
