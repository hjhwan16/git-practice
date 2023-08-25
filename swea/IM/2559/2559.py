n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0
ans = float('-inf')

for i in range(n-k):
    max_v = max_v - arr[i] + arr[k-1]
    if max_v > ans:
        ans = max_v
print(ans)