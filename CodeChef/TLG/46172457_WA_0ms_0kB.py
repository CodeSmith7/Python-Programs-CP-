t = int (input ())
one = 0 
two = 0
mlead = 0
lead = 0
for i in range(t):
    a,b  = map (int,input().split())
    rlead = abs (a-b)
    if rlead > mlead:
        mlead = rlead
        w = 1 if a > b else 2
print (w ,mlead)