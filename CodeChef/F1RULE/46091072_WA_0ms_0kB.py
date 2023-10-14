t = int (input())
for i in range(t):
    a,b = map(int,input().split())

    if b < 1.07 * a:
        print ("YES")
    else:
        print ("NO")
    