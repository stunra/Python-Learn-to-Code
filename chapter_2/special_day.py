# https://dmoj.ca/problem/ccc15j1

month = int(input())
day = int(input())

if month > 2:
    print("After")
elif month == 2:
    if day > 18:
        print("After")
    elif day == 18:
        print("Special")
    else:
        print("Before")
elif month == 1:
    print("Before")

