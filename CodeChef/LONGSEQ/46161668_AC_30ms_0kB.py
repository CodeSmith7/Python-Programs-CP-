t = int (input())
for _ in range(t):
  n = input()
  if (n.count('1') == 1 or n.count('0') == 1):
    print("Yes")
  else:
    print("No")

