def isArmstrong(n):
    d = len(str(n))
    n1 = n
    sumi = 0
    while(n > 0):
        dig = n%10
        sumi += dig**d
        n = n//10
    return sumi    
   
n = int(input())
res = isArmstrong(n)
if n1 == res:
        print ("YES")
else:
    print("NO")