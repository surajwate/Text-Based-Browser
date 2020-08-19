# Read test.txt and print the first letter from each line.
# Close the file

file = open('test.txt')
file_data = file.readlines()
for line in file_data:
    print(line[0])

file.close()