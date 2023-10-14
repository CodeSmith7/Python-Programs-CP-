A = set(map(int,input().split()))
n = int(input())
k = True
for i in range(n):
    s = set(map(int,input().split()))
    if A - s == set():
        k = False
    else:    
        k = k and s.issubset(A)
    
print (k)