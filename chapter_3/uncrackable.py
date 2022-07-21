# https://dmoj.ca/problem/wc17c3j3

import sys

password = input()
lower = 0
upper = 0
digit = 0

if len(password) < 8 or len(password) > 12:
    print("Invalid")
    sys.exit()

for l in password:
    if not(l.isupper() or l.islower() or l.isdigit()):
        print("Invalid")
        sys.exit()
    elif l.isupper():
        upper += 1
    elif l.islower():
        lower += 1
    elif l.isdigit():
        digit += 1

if lower >= 3 and upper >= 2 and digit >= 1:
    print("Valid")
else:
    print("Invalid")

