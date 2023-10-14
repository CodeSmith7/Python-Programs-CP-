n, k = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
ls = lst[k-1]
count = 0
for i in lst:
    if i >= ls and (i>0 and lst_1>0):
        count += 1
print(count)