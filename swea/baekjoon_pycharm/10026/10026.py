import sys
sys.stdin = open('input.txt')

# 적록 색약은 R과 G를 구별하지 못함.
# R과 G는 0으로 B는 1인 2차원 배열 만들어 주고 dfs

N = int(input())

arr = []
# 2차원 배열 만들기
for _ in range(N):
    temp = list(str(input()))
    arr.append(temp)

visited = [[0] * N for _ in range(N)]
stack = []

nocolor = 0 # 적록 색약이 아닌 사람
color = 0 # 적록 색약인 사람

# 상하 좌우 이동용
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 탐색 시작 (적록 색약이 아닌 사람)
for i in range(N):
    for j in range(N):
        # 방문한 적이 없다면 순환
        if visited[i][j] == 0:
            # 시작점의 정보를 반환
            x, y = i, j
            col = arr[x][y]
            # 시작 점 방문 처리
            visited[x][y] = 1
            # 돌아야지
            while True:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 지도 밖으로 안나가고 col이 같으면서 방문한 적이 없을 때
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == col and visited[nx][ny] == 0:
                        stack.append((x, y))
                        x, y = nx, ny
                        # 방문 처리
                        visited[x][y] = 1
                        break
                else:
                    if stack:
                        x, y = stack.pop()
                    else:
                        nocolor +=1
                        break

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0] * N for _ in range(N)]
stack = []

for i in range(N):
    for j in range(N):
        # 방문한 적이 없다면 순환
        if visited[i][j] == 0:
            # 시작점의 정보를 반환
            x, y = i, j
            col = arr[x][y]
            # 시작 점 방문 처리
            visited[x][y] = 1
            # 돌아야지
            while True:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 지도 밖으로 안나가고 col이 같으면서 방문한 적이 없을 때
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == col and visited[nx][ny] == 0:
                        stack.append((x, y))
                        x, y = nx, ny
                        # 방문 처리
                        visited[x][y] = 1
                        break
                else:
                    if stack:
                        x, y = stack.pop()
                    else:
                        color +=1
                        break

print(nocolor, color)

# 함수로 구현했으면 더 편했을 듯?
