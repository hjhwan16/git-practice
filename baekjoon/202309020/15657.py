# N개의 자연수에서 M개를 고른 수열
# 같은 수열을 여러번 골라도 됨
# 고른 수열은 오름차순

def backtracking(cnt):
    # 기저조건
    if len(path) == M:
        print(*path)
        return
    # 돌기 전
    for num in arr:
        if path and num < path[-1]:
            continue
        path.append(num)
        backtracking(cnt + 1)
        path.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []
backtracking(0)