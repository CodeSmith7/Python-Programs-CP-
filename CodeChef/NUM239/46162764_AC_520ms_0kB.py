t = int (input())
for _ in range(t):
  l,r = map(int,input().split())
  li = [2,3,9]
  c = 0
  for i in range(l,r+1):
    if i%10 in li:
      c += 1
  print(c)    

