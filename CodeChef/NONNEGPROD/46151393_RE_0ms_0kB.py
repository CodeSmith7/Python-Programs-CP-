T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    negative_count = sum(1 for a in A if a < 0)
    zero_count = A.count(0)
    min_negative = min(a for a in A if a != 0)
    if negative_count % 2 == 0 or zero_count > 0:
        print(0)
    else:
        print(1)
