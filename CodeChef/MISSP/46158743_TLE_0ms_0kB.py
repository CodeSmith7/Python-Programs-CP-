t = int (input ())
for i in range (t):
    n = int (input ())
    l = []
    for i in range(n):
        ele = int (input ())
        l.append(ele)
        

    for i in l:
        if l.count(i) == 1:
            print(i)