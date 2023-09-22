# N개의 자연수 중에서 M개를 고른 순열
# 중복되는 수열은 한번 만 출력
from copy import deepcopy
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []
path_idx = []
result = set()
def backtracking(cnt):
    # 기저조건
    if len(path) == M:
        # in 연산은 시간을 많이 먹음
        temp = deepcopy(path)
        result.add(tuple(temp))
        # print(*path)
        return
    # 반복문 and 재귀
    for i in range(len(arr)):
        if i in path_idx:
            continue
        path.append(arr[i])
        path_idx.append(i)
        backtracking(cnt+1)
        path.pop()
        path_idx.pop()

backtracking(0)
lst = sorted(list(result))
for i in lst:
    print(*i)