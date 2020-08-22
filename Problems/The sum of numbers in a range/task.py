def range_sum(numbers, start, end):
    numbers = [int(i) for i in numbers]
    plus = [int(i) for i in numbers if int(start) <= i <= int(end)]
    return sum(plus)


input_numbers = input().split()  # ...
a, b = input().split()  # ...
print(range_sum(input_numbers, a, b))
