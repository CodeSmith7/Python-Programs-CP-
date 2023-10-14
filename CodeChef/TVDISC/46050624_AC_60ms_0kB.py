t = int (input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    one = a-c
    two = b-d
    if (one < two):
        print("First")
    elif (one > two):
        print("Second")
    else:
        print("any")