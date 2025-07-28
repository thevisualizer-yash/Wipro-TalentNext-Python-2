'''
1. Write a program to find check if a string has only octal digits. Given string ['789','123','004']
'''

def is_octal(s):
    for char in s:
        if char < '0' or char > '7':
            return False
    return True

strings = ['789', '123', '004']

for s in strings:
    if is_octal(s):
        print(f"'{s}' is an octal string.")
    else:
        print(f"'{s}' is NOT an octal string.")

'''
2. Extract the user id, domain name and suffix from the following email addresses.emails = """zuck@facebook.comsunder33@google.comjeff42@amazon.com"""
'''

import re

emails = """zuck@facebook.comsunder33@google.comjeff42@amazon.com"""

email_list = re.findall(r'\b[\w.]+@[\w.]+\.\w+\b', emails)

for email in email_list:
    match = re.match(r'([\w.]+)@([\w.]+)\.(\w+)', email)
    if match:
        user_id, domain, suffix = match.groups()
        print(f"Email: {email}")
        print(f"User ID: {user_id}, Domain: {domain}, Suffix: {suffix}\n")


'''
3. Split the following irregular sentence into proper words sentence = """A, very very; irregular_sentence""" ## expected outout : A very very irregular sentence
'''

import re

sentence = """A, very very; irregular_sentence"""

cleaned = re.sub(r'[^a-zA-Z]+', ' ', sentence)

final_sentence = ' '.join(cleaned.split())

print(final_sentence)

'''
4. Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
tweet = Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt rstats  desired_output = 'Good advice What I would do differently if I was learning to code today'

'''

import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

tweet = re.sub(r'\bRT\b|\bcc\b:?', '', tweet)

tweet = re.sub(r'http\S+', '', tweet)

tweet = re.sub(r'@\w+|#\w+', '', tweet)

tweet = re.sub(r'[^\w\s]', '', tweet)

tweet = ' '.join(tweet.split())

print(tweet)

'''
5. Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html Code to retrieve the HTML page is given below: import requests 
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text # html text is contained here desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 
'This is a new paragraph! ', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
'''

import requests
from bs4 import BeautifulSoup

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text

soup = BeautifulSoup(html, 'html.parser')

texts = [text.strip() for text in soup.stripped_strings]

print(texts)

'''
6. Given below list of words, identify the words that begin and end with the same character. civic trust widows maximum museums aa as
'''

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

result = [word for word in words if word[0] == word[-1]]

print(result)


