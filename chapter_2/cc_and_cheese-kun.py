# https://dmoj.ca/problem/dmopc16c1p0

W = int(input())
C = int(input())

M = ""
if W == 3 and C >= 95:
    M = "absolutely"
elif W == 1 and C <= 50:
    M = "fairly"
else:
    M = "very"

print("C.C. is " + M + " satisfied with her pizza.")
