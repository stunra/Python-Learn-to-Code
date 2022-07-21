# https://dmoj.ca/problem/coci16c1p1

megabytes = int(input())
months = int(input())
spent = 0

for x in range(months):
    spent += int(input())

print((months * megabytes + megabytes) - spent)

