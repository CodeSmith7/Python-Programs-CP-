t = int (input())
for i in range(t):
    n = int (input())
    l = set(map(int,input().split()))
    l =list(l)
    l.sort()
    #print (l)
    print(l[-1] + l[-2])
    