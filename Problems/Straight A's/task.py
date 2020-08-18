# put your python code here
grades = input()

total_a = grades.count('A')
total_count = len(grades.replace(" ", ""))

fraction = round(total_a / total_count, 2)

print(fraction)
