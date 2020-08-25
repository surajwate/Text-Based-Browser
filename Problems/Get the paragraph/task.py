import requests

from bs4 import BeautifulSoup

word = input()
story_link = input()

r = requests.get(story_link)

soup = BeautifulSoup(r.content, 'html.parser')

paragraph = soup.find_all('p')
count = 1

for p in paragraph:
    if word in p.getText():
        print(p.getText())
