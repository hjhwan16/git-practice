import sys
sys.stdin = open('input.txt')
# 단지 번호 붙이기 / DFS / 20230811

# 정사각형 모양의 지도 1:집 0:집x

# 연결된 집의 모임 -> 단지 / 단지의 번호

# 지도를 입력해 단지수를 출력 / 각 단지에 속하는 집의 수를 오름차순으로 정렬

N = int(input())
# 지도 2차원 배열 입력받기
arr = []
for _ in range(N):
    temp = list(str(input()))
    arr.append(temp)

# 인접 행렬 or 인접 리스트 만들기. 말고 그냥 주어진 map 사용?
cnt = 0 # 단지 수
homes = [] # 단지에 속하는 집의 수

visited = [[0] * N for _ in range(N)]
stack = []
    # 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):

    for j in range(N):
        home = 0
        # 집인 경우에!
        if arr[i][j] == '1' and visited[i][j] == 0:
            x, y = i, j
            # 방문 처리
            visited[x][y] = 1
            home += 1
            while True:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == '1':
                        stack.append((x, y))
                        # 방문 처리
                        x, y = nx, ny
                        visited[x][y] = 1
                        home += 1
                        break
                else:
                    if stack:
                        x, y = stack.pop()
                    else:
                        cnt += 1
                        homes.append(home)
                        break

print(cnt)
homes.sort()
for i in homes:
    print(i)

