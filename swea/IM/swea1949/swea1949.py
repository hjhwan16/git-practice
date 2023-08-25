import sys
sys.stdin = open('input.txt')

# 시작점 찾는 함수 max 값 먼저 찾고 그 지점 반환
def max_length(arr, N):
    max_len = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= max_len:
                max_len = arr[i][j]
    return max_len


# 시작점 찾는 함수
def start(arr, N, max_len):
    start_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_len:
                start_list.append((i, j))
    return start_list


# 탐색함수
def dfs(si, sj, N, arr, K):
    max_route = 0
    stack = []
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    use_K = False
    K_used = (-1, -1)
    K_return = (-1, -1)
    while True:
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            # 박스 안에 들어오면
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                # K를 사용하지 않아도 되는 경우
                if arr[ni][nj] < arr[si][sj]:
                    stack.append((si, sj))
                    visited[ni][nj] = visited[si][sj] + 1
                    if visited[ni][nj] > max_route:
                        max_route = visited[ni][nj]
                    si, sj = ni, nj
                    break
                # K를 사용하지 않고 K를 사용하면 가능한 경우
                else:
                    if not use_K:
                        if arr[ni][nj] - K < arr[si][sj]:
                            use_K = True
                            K_used = (si, sj)
                            for m in range(1, K+1):
                                if arr[ni][nj] - m < arr[si][sj]:
                                    arr[ni][nj] -= m
                                    K_return = [ni, nj, m]
                                    break
                            stack.append((si, sj))
                            visited[ni][nj] = visited[si][sj] + 1
                            if visited[ni][nj] > max_route:
                                max_route = visited[ni][nj]
                            si, sj = ni, nj
                            break
        else:
            if stack:
                si, sj = stack.pop()
                if (si, sj) == K_used:
                    use_K = False
                if (si, sj) == K_return[:2]:
                    arr[si][sj] += K_return[2]
            else:
                break
    return max_route


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # 봉우리 지점 찾기
    max_len = max_length(arr, N)
    # 시작점 찾기 list 내부에 (i, j) 형태로 저장 되어 있음
    start_point = start(arr, N, max_len)
    ans = 0
    for si, sj in start_point:
        # 각 경우에서 최대 이동거리 temp
        temp = dfs(si, sj, N, arr, K)
        if temp > ans:
            ans = temp

    print(f'#{tc} {ans}')
