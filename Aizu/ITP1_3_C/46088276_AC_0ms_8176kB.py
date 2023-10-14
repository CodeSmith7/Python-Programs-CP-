#0221MCA230
while True:
    a,b = map (int,input().split())
    if a == 0 and b == 0:
        break
    num1 = [a,b]
    num1.sort()
    print (num1[0],num1[1])
    