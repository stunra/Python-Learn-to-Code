# https://dmoj.ca/problem/ccc15j2

happy = 0
sad = 0

sample = input()

y = 0
for x in sample:
    if x == ':':
        if sample[y + 1] == '-':
            if sample[y + 2] == ')':
                happy += 1
            elif sample[y + 2] == '(':
                sad += 1
    y += 1

if happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
elif happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
