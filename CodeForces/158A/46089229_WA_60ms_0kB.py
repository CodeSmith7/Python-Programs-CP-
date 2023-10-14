a,b = map(int,input().split())

l = [int(x) for x in input().split()]
c = 0
for i in l:
    if i > b:
        c = c + 1
print(c)
    