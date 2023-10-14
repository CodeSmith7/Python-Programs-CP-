t = int(input())
d = {}
for i in range(t):
    k, v = input().split()
    d[k] = v
for i in range(t):
    a = input()
    if a in d:
        print("{}={}".format(a, d[a]))
    else:
        print("Not found")