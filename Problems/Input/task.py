# Read a line from input and write it to the file input.txt.

data = input()

file = open('input.txt', 'w', encoding='utf-8')
file.write(data)
file.close()
