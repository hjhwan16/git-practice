import sys
sys.stdin = open('input.txt')

# 스택 / 20230810 / 길 찾기
# 길은 일방 통행
# 길이 이어져 있는지?
# 정점의 갯수는 98개를 넘지 않음
def dfs(s, g, adj_m):
    stack = []
    visited = [0] * 100
    # 시작점 방문
    visited[s] = 1
    ans = 0
    while True:
        for w in range(1, 100):
            if adj_m[s][w] == 1 and visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                if s == g:
                    ans = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    return ans

T = 10

for tc in range(1, T+1):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_m = [[0]*100 for _ in range(100)]
    for i in range(N):
        s, g = arr[2*i], arr[2*i + 1]
        adj_m[s][g] = 1

    # 0에서 출발해서 99까지 갈 수 있음?
    result = dfs(0, 99, adj_m)
    print(f'#{tc} {result}')
