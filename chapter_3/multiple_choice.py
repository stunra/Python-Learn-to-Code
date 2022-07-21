# https://dmoj.ca/problem/ccc11s2

N = int(input())
ans = [input() for x in range(N)]
correct = [input() for x in range(N)]
score = 0

for x in range(N):
    if ans[x] == correct[x]:
        score += 1

print(score)

