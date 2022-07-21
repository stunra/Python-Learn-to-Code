# https://dmoj.ca/problem/ccc18j2

spaces = int(input())
yesterday = input()
today = input()
length = len(yesterday)
count = 0

for x in range(length):
    if yesterday[x] == 'C' and today[x] == 'C':
        count += 1

print(count)
