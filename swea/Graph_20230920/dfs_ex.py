# DFS는 스택과 재귀 두가지 방법으로 구현 가능

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

# stack 버젼
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 방문한 지점이라면
        if now in visited:
            continue
        visited.append(now)

        # 갈 수 있는 곳들을 stack에 추가
        for next in range(5):
            # 연결이 안되어 있다면 컨티뉴
            if graph[now][next] == 0:
                continue

            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)

    return visited

result = dfs_stack(0)
print(*result)

# 재귀 버젼
visited = [0] * 5
path = []

def dfs_recur(now):
    visited[now] = 1
    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next] == 1:
            continue
        dfs_stack(next)
    # 기저조건

    # 들어가기 전
    # 함수 호출
    # 돌아와서