from collections import deque

my_stack = deque()

total_char = int(input())
for _i in range(total_char):
    ch = input()
    my_stack.append(ch)

for _i in range(total_char):
    print(my_stack.pop())