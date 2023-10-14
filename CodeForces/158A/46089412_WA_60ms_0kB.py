a,b = map(int,input().split())

l = [int(x) for x in input().split()]
c = 0
w = l[b-0]
for i in l:
    if i>=w:
        c = c+1
print (c)