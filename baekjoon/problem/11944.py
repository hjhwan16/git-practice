N, M = map(int, input().split())

ans = str(N) * N

if len(ans) > M:
    ans = ans[:M]
print(ans) 