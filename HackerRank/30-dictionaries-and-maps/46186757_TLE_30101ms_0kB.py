t = int (input())
d = {}
for i in range(t):
    k,v = map(str,input().split())
    d[k] = v
l  = list(d.keys())
for i in range(t):
    a = input()
    if a in l:
        print("{}={}".format(a,d[a]))
    else:
        print("Not found")


    