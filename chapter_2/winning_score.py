# https://dmoj.ca/problem/ccc19j1

A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())

A_score = (A3 * 3) + (A2 * 2) + (A1)
B_score = (B3 * 3) + (B2 * 2) + (B1)

if A_score > B_score:
    print('A')
elif B_score > A_score:
    print('B')
else:
    print('T')
