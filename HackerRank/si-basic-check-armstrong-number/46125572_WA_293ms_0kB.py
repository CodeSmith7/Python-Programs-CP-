def isArmstrong(n):
    sumi = 0
    n1 = n
    while(n > 0):
        dig = n%10
        sumi += dig**3
        n = n//10
    if n1 == sumi:
        print ("YES")
    else:
        print("NO")    
   
n = int(input())
isArmstrong(n)