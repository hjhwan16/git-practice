from itertools import combinations
# 회전 초밥 / 20230912
N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr *= 2
ans = -1
# l = len(set(arr))
# if l < k:
#     ans = l
# else:
#     ans = k


for i in range(N):
    temp = set(arr[i:i+k] + [c])
    # print(temp)
    m = len(temp)
    if m > ans:
        ans = m
print(ans)




