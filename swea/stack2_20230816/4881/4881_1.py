import sys

# visited 사용
def search(col, cnt):
    # cnt를 매개변수로 사용
    global result
    
    if cnt > result: # 임시값이 최대값 보다 크다면, 더 이상 유망하지 않음.
        return

    if col == N:
        if cnt < result:
            result = cnt

    else:
        for row in range(N):
            if not visited[row]: # 방문하지 않은 열이라면
                visited[row] = 1 # 방문 표시
                search(col + 1, cnt + arr[col][row])
                visited[row] = 0 # 방문 표시 초기화

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 10 * N
    
    search(0, 0)




