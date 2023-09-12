# 한 줄로 서기 / 20230911

N = int(input())
arr = list(map(int, input().split()))
ans_arr = [0] * N
0
for i in range(1, N+1):
    cnt = 0
    idx = arr[i-1]
    for k in range(N):
        if ans_arr[k] == 0 and cnt == idx:
            ans_arr[k] = i
            break
        elif ans_arr[k] == 0:
            cnt += 1
print(*ans_arr)

