# https://dmoj.ca/problem/coci18c3p1

text = input()

H = 0
O = 0
N = 0
I = 0

for c in text:
    if c == 'H' and H == I:
        H += 1
    elif c == 'O' and O == (H - 1):
        O += 1
    elif c == 'N' and N == (O - 1):
        N += 1
    elif c == 'I' and I == (N - 1):
        I += 1

print(I)
