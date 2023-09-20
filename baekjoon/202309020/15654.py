# N과 M(5) / 백트래킹 문제

# N개의 자연수 중에서 M개를 고른 수열
def backtracking(cnt):
    # 기저조건
    if len(path) == M:
        print(*path)
        return
    # 재귀 돌귀 전
    for num in arr:
        if num in path:
            continue
        path.append(num)
    # 재귀함수 호출
        backtracking(cnt+1)
    # 재귀 돈 다음
        path.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []
backtracking(0)