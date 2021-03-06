import os
import sys
from collections import deque
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

import requests

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


# write your code here


def url_correction(url: str) -> str:
    if url[0:5] != 'https' or url[0:4] != 'http':
        return "https://" + url
    else:
        return url


def file_update(url: str) -> None:
    if "." not in url:
        return None
    try:
        status = requests.get(url_correction(url))
    except:
        status = 400
    if 200 <= status.status_code < 400:
        file.append(url)
    else:
        return None


def get_content(url):
    selected_tags = SoupStrainer(['p', 'li', 'ol', 'ul', 'a'])
    r = requests.get(url_correction(url))
    soup = BeautifulSoup(r.content, 'html.parser', parse_only=selected_tags)

    data = ""

    paragraph = soup.find_all()
    for p in paragraph:
        if p.name == 'a':
            data = data + '\033[34m' + p.text + '\033[39m' + "\n"
        else:
            data = data + p.text

    return (data)


def print_history(history: deque) -> None:
    url = history.pop()
    if url == 'bloomberg.com' or url == 'bloomberg':
        print(bloomberg_com)
    elif url == 'nytimes.com' or url == 'nytimes':
        print(nytimes_com)


args = sys.argv
folder = args[1]

try:
    os.mkdir(folder)  # Create a file which act like tab
except:
    pass

# Get current working directory
current_path = os.getcwd()
# Create a path to save the created files in
path = current_path + '\\' + folder + '\\'

file = ["bloomberg.com", "nytimes.com"]
url = input()
file_update(url)
history = deque()

while url != 'exit':
    # Condition to check if we have the url in our data (file)
    if "." in url and url in file:
        history.append(url)
        name = url.split(".")
        # Create a file_name to save file in tab(folder)
        file_name = ".".join(name[0:-1])
        content = get_content(url)
        print(content)

        with open(path + file_name + '.txt', 'w', encoding='utf-8') as web_file:  # Create a file to save content
            web_file.write(content)
            file.append(file_name)

    elif url == 'nytimes':
        history.append(url)
        print(nytimes_com)

    elif url == 'bloomberg':
        history.append(url)
        print(bloomberg_com)

    elif url == 'back':
        history.pop()  # pop the current url for printing history
        if len(history) >= 1:
            print_history(history)
        else:
            pass

    elif "." not in url or url not in file:
        print("error: Please enter correct url.")

    url = input()
    if url not in file and url != "exit":
        file_update(url)
