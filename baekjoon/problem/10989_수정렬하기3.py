# 수 정렬하기 3
# 수의 범위가 적다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다.
# list.sort() 가 오래걸림
import sys
input = sys.stdin.readline

N = int(input())
cnt_list = [0] * (10001)

# num을 입력받을 때 마다 cnt 하나씩 올리기.
for i in range(N):
    num = int(input())
    cnt_list[num] += 1

for k in range(10001):
    cnt = cnt_list[k]
    for j in range(cnt):
        print(k)

