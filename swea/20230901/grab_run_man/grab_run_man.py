import sys
sys.stdin = open('input.txt')
from collections import deque

# t1 출발지, k 방향, t2 도착지
def isConnect(t1, k, t2):
    if t1 == 1:
        if k == 0:
            # 왼쪽과 연결
            if t2 in [1, 3, 6, 7]:
                return True

        elif k == 1:
            # 오른쪽과 연결
            if t2 in [1, 3, 4, 5]:
                return True

        elif k == 2:
            # 위와 연결
            if t2 in [1, 2, 4, 7]:
                return True

        elif k == 3:
            # 아래와 연결
            if t2 in [1, 2, 5, 6]:
                return True

        else:
            return False

    elif t1 == 2:
        if k == 2:
            if t2 in [1, 2, 4, 7]:
                return True

        elif k == 3:
            if t2 in [1, 2, 5, 6]:
                return True

        else:
            return False

    elif t1 == 3:
        if k == 0:
            if t2 in [1, 3, 6, 7]:
                return True

        elif k == 1:
            if t2 in [1, 3, 4, 5]:
                return True

        else:
            return False

    elif t1 == 4:
        if k == 0:
            if t2 in [1, 3, 6, 7]:
                return True

        elif k == 3:
            if t2 in [1, 2, 5, 6]:
                return True

        else:
            return False

    elif t1 == 5:
        if k == 0:
            if t2 in [1, 3, 6, 7]:
                return True

        elif k == 2:
            if t2 in [1, 2, 4, 7]:
                return True

        else:
            return False

    elif t1 == 6:
        if k == 1:
            if t2 in [1, 3, 4, 5]:
                return True

        elif k == 2:
            if t2 in [1, 2, 4, 7]:
                return True

        else:
            return False

    elif t1 == 7:
        if k == 1:
            if t2 in [1, 3, 4, 5]:
                return True

        elif k == 3:
            if t2 in [1, 2, 5, 6]:
                return True

        else:
            return False
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   # 터널 지도의 세로 N, 가로 M, 맨홀뚜껑의 위치(R, C) 시간 :L
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # print(arr)
    # bfs 로 이동
    queue = deque()
    visited = [[0]*M for _ in range(N)]
    queue.append((R, C, arr[R][C])) # 위치와 구조물 정보
    visited[R][C] = 1
    while queue:    # 시작점도 한시간 이기 때문에
        i, j, t = queue.popleft()
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 지도 안에 있고 방문한 적이 없으면서
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if isConnect(t, k, arr[ni][nj]):# 파이프가 연결 된 경우
                    queue.append((ni, nj, arr[ni][nj]))
                    visited[ni][nj] = visited[i][j] + 1
            
    # print(visited)
    ans = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                ans += 1
    print(f'#{tc} {ans}')
