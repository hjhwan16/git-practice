N, M = map(int, input().split())

def backtracking():
    # 기저조건
    if len(path) == M:
        print(*path)
        return
    # 반복문
    for i in range(1, N+1):
        # print(path, i)
        if path and i >= path[-1]:
            path.append(i)
            backtracking()
            path.pop()
        if not path:
            path.append(i)
            backtracking()
            path.pop()


path = []
backtracking()