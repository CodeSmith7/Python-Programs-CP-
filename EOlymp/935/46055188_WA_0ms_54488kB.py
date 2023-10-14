n = int (input())
if n < 0:
    n = abs(n)
s = str(n)
s = s[::-1]
s =int(s)
while s > 0:
    d = s%10
    print (d)
    s = s//10