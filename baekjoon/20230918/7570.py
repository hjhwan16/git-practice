# 줄 세우기
N = int(input())
from copy import deepcopy
# N이 홀수인경우 중간값 가만히, 중간값 왼쪽 앞으로(작아지는 순서로), 중간값 오른쪽 뒤로(커지는 순서로)
# N이 짝수인경우 중간값 왼쪽 앞으로, 중간값 오른쪽 뒤로

arr = list(map(int, input().split()))
temp_lst = [0] * (N+1)
for i in range(N):
    temp_lst[arr[i]] = i
# print(temp_lst)
ans1 = 0
ans2 = 0
# N이 홀수인경우
cnt_l = 0
cnt_r = 0
mid = N // 2 + 1
# print(mid)
temp_lst1 = deepcopy(temp_lst)
i = mid
j = mid
while i < N:
    # print(i)
    if temp_lst1[i+1] < temp_lst1[i]:
        ans1 += 1
        cnt_r += 1
        temp_lst1[i+1] = N + cnt_r
        i = mid
    i += 1
while j > 0:
    if temp_lst1[j-1] > temp_lst1[j]:
        ans1 += 1
        cnt_r += 1
        temp_lst1[j-1] = 0 - cnt_r
        j = mid
    j -= 1

temp_lst2 = deepcopy(temp_lst)
for j in range(mid, 1, -1):
    # print(j)
    if temp_lst2[j-1] > temp_lst2[j]:
        ans2 += 1
        cnt_r += 1
        temp_lst2[j-1] = 0 - cnt_r
for i in range(mid, N):
    # print(i)
    if temp_lst2[i+1] < temp_lst2[i]:
        ans2 += 1
        temp_lst2[i+1] = N + cnt_r
        cnt_r += 1



ans = min(ans1, ans2)
print(ans)