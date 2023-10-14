n = int(input())
l = {}
for i in range(n):
    a = input()
    l[a] = l.get(a, 0) + 1
l1 = list(l.keys())
l1.sort()
l2 = {i: l[i] for i in l1}
m = max(l2.values())

for i in l1[::-1]:
    if l2[i] == m:
        print(i)
        break