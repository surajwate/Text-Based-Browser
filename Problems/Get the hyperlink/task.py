import requests

from bs4 import BeautifulSoup

act = input()
link = input()

r = requests.get(link)

soup = BeautifulSoup(r.content, 'html.parser')

a_tags = soup.find_all('a')

for link in a_tags:
    if link.get('href'):
        if act in link.get('href'):
            print(link.get('href'))