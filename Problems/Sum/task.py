""" 
You have the file sums.txt. It has multiple lines that contain two numbers separated by whitespace. All numbers are positive.
For example:

9 61
15 47
2 1

Write a program that reads this file and print the sum of numbers on each line. So, if the file has n lines, you should print n sums, each on a separate line.

"""

file = open("sums.txt")
for line in file:
    numbers = line.split()
    sums = int(numbers[0]) + int(numbers[1])
    print(sums)

file.close()
