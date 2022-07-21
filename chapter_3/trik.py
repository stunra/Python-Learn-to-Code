# https://dmoj.ca/problem/coci06c5p1

moves = input()

cup1 = 1
cup2 = 0
cup3 = 0

for l in moves:
    if l == "A" and (cup1 == 1 or cup2 == 1):
        cup1, cup2 = cup2, cup1
    elif l == "B" and (cup2 == 1 or cup3 == 1):
        cup2, cup3 = cup3, cup2
    elif l == "C" and (cup3 == 1 or cup1 == 1):
        cup1, cup3 = cup3, cup1

if cup1 == 1:
    print(1)
elif cup2 == 1:
    print(2)
elif cup3 == 1:
    print(3)


