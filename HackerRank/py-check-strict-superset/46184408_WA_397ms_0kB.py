A = set(map(int,input().split()))
n = int(input())
k = True
for i in range(n):
    s = set(map(int,input().split()))
    k = k and s in A
    
print (k)