import re  # import the library for regular expressions
import requests  # importing library  URL requests
from bs4 import BeautifulSoup  # installing package that makes an htt request

url = "https://www.bbc.co.uk/news/uk-politics-49651969"
response = requests.get(url)
website_string = str(BeautifulSoup(response.text, "html.parser"))

brex_find = re.findall(r"((brexit)|(Brexit)|BREXIT)", website_string)
# use a regular expression to find all instances of brexit or Brexit and store them in tuples.

brex_find_dict = {}  # creates empty dictionary

for phone in brex_find:

    if phone[0] in brex_find_dict:  # increase counter when the word brexit is found
        brex_find_dict[phone[0]] += 1

    else:
        brex_find_dict[phone[0]] = 1

sort_brex_finds = sorted(brex_find_dict.items(), key=lambda x: x[1], reverse=True)  # sorts the list
# of domains from most to least popular (switches the key from x[0] (the key) to x[1] (the value).)

low = int(input("Please enter the minimum frequency you require:"))
for number in sort_brex_finds:
    if number[1] < low:  # doesn't print any instances where the frequency is less than the user requested.
        break
    else:
        print( str(number[0]), "\n Frequency:", str(number[1]))  # printing formatting
