from collections import deque

ops = int(input())

book_to_read = deque()
book_read = []

for _i in range(ops):
    book = input()
    if book.split()[0] == 'BUY':
        # split the input and join it by space from second word and append it to list.
        book_to_read.append(" ".join(book.split()[1:]))
    if book == 'READ':
        book_read.append(book_to_read.pop())

for i in book_read:
    print(i)
