N = int(input())
arr = []
ans = 0
for i in range(1, N-1):
    for j in range(i, N-i):
        # print(i, j, N - i - j)
        if max(i, j, N - i - j) == N-i-j and N-i-j < i + j:
            ans += 1

print(ans)
