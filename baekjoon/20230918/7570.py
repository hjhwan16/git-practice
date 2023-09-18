# 줄 세우기
N = int(input())

# N이 홀수인경우 중간값 가만히, 중간값 왼쪽 앞으로(작아지는 순서로), 중간값 오른쪽 뒤로(커지는 순서로)
# N이 짝수인경우 중간값 왼쪽 앞으로, 중간값 오른쪽 뒤로

arr = list(map(int, input().split()))
temp_lst = [0] * (N+1)
for i in range(N):
    temp_lst[arr[i]] = i
# print(temp_lst)
ans = 0
# N이 홀수인경우
if N % 2 == 1:
    cnt_l = 0
    cnt_r = 0
    mid = N // 2 + 1
    # print(mid)
    for i in range(mid, N):
        # print(i)
        if temp_lst[i+1] < temp_lst[i]:
            ans += 1
            cnt_r += 1
            temp_lst[i+1] = N + cnt_r
    for j in range(mid, 1, -1):
        # print(j)
        if temp_lst[j-1] > temp_lst[j]:
            ans += 1
            cnt_r += 1
            temp_lst[j-1] = 0 - cnt_r

else:
    left = N // 2
    right = left + 1
    cnt_l = 0
    cnt_r = 0
    # print(mid)
    for i in range(right, N):
        # print(i)
        if temp_lst[i + 1] < temp_lst[i]:
            ans += 1
            cnt_r += 1
            temp_lst[i + 1] = N + cnt_r
    for j in range(left, 1, -1):
        # print(j)
        if temp_lst[j - 1] > temp_lst[j]:
            ans += 1
            cnt_r += 1
            temp_lst[j - 1] = 0 - cnt_r

print(ans)