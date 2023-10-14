a,b = map(int,input().split())
li = list(map (int,input().split()))
for _ in range(b):
    l,r = map(int,input().split())
    print(sum(li[l-1:r]))
    