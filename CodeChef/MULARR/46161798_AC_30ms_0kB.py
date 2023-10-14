t = int (input())
for i in range(t):
   
    n = int (input())
    l = list(map(int,input().split()))
    m = 1
    for i in l:
        m = m * i
    print(m)
    