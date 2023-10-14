#abhi
t = int (input ())
for i in range (t):
    n = int (input ())
    l = []
    ans = 0 
    for i in range(n):
        ele = int (input ())
        l.append(ele)
        ans = ans ^ ele
    print (ans)