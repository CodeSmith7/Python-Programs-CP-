n = int(input())
count = 0
for i in range(n):
    a,b,c = map(int,input().split())
    sumi  = a+b+c
    if sumi > 1:
        count += 1
print (count)
  #jk