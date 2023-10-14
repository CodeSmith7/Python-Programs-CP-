n = int (input())
if n < 0:
    n = abs(n)
while n>0:
    d = n%10
    n = n // 10
print (d)
    