e = int(input())
eng = set(map(int,input().split()))
f = int(input())
fre = set(map(int,input().split()))

c = eng ^ fre
print (len(c))