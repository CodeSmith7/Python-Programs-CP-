tsec = int(input())

h = tsec // (60*60)
rsec = tsec - h*60*60
min = rsec // 60 
sec = rsec - min * 60 

print("{}:{}:{}".format(h,min,sec))