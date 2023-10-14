import math
t = int (input())
for i in range(t):
    a,b = map(int,input().split())
    totalSlice = a*b 
    print(math.ceil(totalSlice/4))