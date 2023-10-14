t = int (input())
for i in range(t):
    n1 = int (input())
    A = set(map(int,input().split()))
    n1 = int (input())
    B = set(map(int,input().split()))
    print (A.issubset(B))