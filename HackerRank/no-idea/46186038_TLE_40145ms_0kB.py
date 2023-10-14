n1,n1 = map(int,input().split())
arr = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
happy = 0
for i in A:
    happy += arr.count(i)
for j in B:
    happy -= arr.count(j)
print(happy)