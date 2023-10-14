#0221MCA230
t  = int(input())
for i in range(t):
    n = int(input())
    om = list(map(int,input().split()))
    addy = list(map(int,input().split()))
    so = 0
    sa = 0
    omSum = so
    adSum = sa
    
    for i in range (n):
        if om[i] != 0:
            so += 1
        else:
            omSum = so
            so = 0
        if addy[i] != 0:
            sa += 1
        else:
            adSum = sa
            sa = 0
        
    
    
    adSum = max(adSum,sa)
    omSum = max(omSum,so)
            
    if omSum < adSum:
        print("Addy")
    elif omSum > adSum:
        print("Om")
    else:
        print ("Draw")
