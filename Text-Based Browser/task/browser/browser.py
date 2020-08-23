import sys
import os
from collections import deque

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
history = deque()

def print_history(history: deque) -> None:
    url = history.pop()
    if url == 'bloomberg.com' or url == 'bloomberg':
        print(bloomberg_com)
    elif url == 'nytimes.com' or url == 'nytimes':
        print(nytimes_com)


while url != 'exit':
    # Condition to check if we have the url in our data (file)
    if "." in url and url in file:
        history.append(url)
        name = url.split(".")
        # Create a file_name to save file in tab(folder)
        file_name = ".".join(name[0:-1])

        content = ""
        if url == "nytimes.com":
            content = nytimes_com
            print(nytimes_com)
        elif url == "bloomberg.com":
            content = bloomberg_com
            print(bloomberg_com)

        with open(path + file_name + '.txt', 'w') as web_file:  # Create a file to save content
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

