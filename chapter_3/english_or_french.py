# https://dmoj.ca/problem/ccc11s1

linecount = int(input())
text = []
for x in range(linecount):
    text.append(input())

tcount = 0
scount = 0

for lines in text:
    for char in lines:
        if char == 'T' or char == 't':
            tcount += 1
        elif char == 'S' or char == 's':
            scount += 1

if tcount > scount:
    print("English")
else:
    print("French")
