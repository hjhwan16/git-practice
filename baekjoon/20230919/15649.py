# 1부터 N까지 자윤수 중에서 중복 없이 M개를 고른 수열
def backtracking(start):
    # 기저조건
    if len(path) == M:
        print(*path)
        return
    # 반복문 and 가지치기
    for i in range(start, N+1):
        path.append(i)
        backtracking(i+1)
        path.pop()




N, M = map(int, input().split())
path = []
visited = [0] * (N+1)
backtracking(1)
