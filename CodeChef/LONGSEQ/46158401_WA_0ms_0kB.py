t = int (input())
for i in range(t):
  n = int(input())
  s = str(n)
  z = s.count('0')
  o = s.count('1')
  print (z,o)
  if z==1 or o ==1  :
    print ("Yes")
  else:
    print ("No") 