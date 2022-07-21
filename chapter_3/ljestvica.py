# https://dmoj.ca/problem/coci12c5p1

# aminor = ["A", "B", "C", "D", "E", "F", "G"]
# cmajor = ["C", "D", "E", "F", "G", "A", "B"]

# amain = ["A", "D", "E"]
# cmain = ["C", "F", "G"]

music = input()
amin = 0
cmaj = 0


if music[0] in ('A', 'D', 'E'):
    amin += 1
elif music[0] in ('C', 'F', 'G'):
    cmaj += 1

for x in range(1, len(music)):
    if music[x] in ('A', 'D', 'E') and music[x - 1] == '|':
        amin += 1
    elif music[x] in ('C', 'F', 'G') and music[x - 1] == '|':
        cmaj += 1

if cmaj == amin:
    if music[-1] == 'A':
        print("A-mol")
    else:
        print("C-dur")
else:
    if amin > cmaj:
        print("A-mol")
    else:
        print("C-dur")







