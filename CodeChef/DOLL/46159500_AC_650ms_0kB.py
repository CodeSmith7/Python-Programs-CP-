t = int (input ())
for i in range (t):
    n,h = map(int,input().split())
    l = list(map(int,input().split()))
    c = 0 
    for i in l:
        if i > h:
            c += 1
    print(c)
    
    