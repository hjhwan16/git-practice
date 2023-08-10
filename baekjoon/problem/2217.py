# 20230810 / 로프

import sys
input = sys.stdin.readline

N = int(input())
arr=[]

for _ in range(N):
    num = int(input())
    arr.append(num)
arr.sort()

max_v = arr[-1]

for idx in range(len(arr[:-1])):
    # print(max_v, (arr[idx]* (N-idx)))
    if max_v < arr[idx] * (N-idx):
        # print('갱신')
        max_v = arr[idx] * (N-idx)

print(max_v)

'''
반례
3
10
5
15

20이 나와야 하는데
15
'''