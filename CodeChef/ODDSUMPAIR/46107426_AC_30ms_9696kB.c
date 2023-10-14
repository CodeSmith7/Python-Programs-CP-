# cook your dish here
t = int(input())
for i in range(t):
    a,b,c = map (int, input().split())
    c = a%2  + b%2 + c%2
    if c > 2 or  c == 0:
        print("NO")
    else:
        print("YES")
        