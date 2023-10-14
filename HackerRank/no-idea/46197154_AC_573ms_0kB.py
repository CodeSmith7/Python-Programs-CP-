n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

elementCounts = {}
for num in arr:
    if num in elementCounts:
        elementCounts[num] += 1
    else:
        elementCounts[num] = 1

happy = 0
for i in A:
    if i in elementCounts:
        happy += elementCounts[i]

for j in B:
    if j in elementCounts:
        happy -= elementCounts[j]

print(happy)
