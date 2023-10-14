T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    if N + K <= M:
        print("Yes")
    else:
        print("No")
