N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
# print(arr)
ans = 0
for i in range(N-1):
    temp = arr.pop()
    if arr[-1] < temp:
        continue
    # 점수가 같거나 크다면
    else:
        ans += arr[-1] - (temp - 1)
        arr[-1] = temp - 1
print(ans)

