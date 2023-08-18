import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    ans = 0 # 수행 후 맨 앞에 있는 숫자
    N, M = map(int, input().split())    # N개의 숫자로 이루어진 수열 맨 앞의 숫자를 맨 뒤로 M번 보냄
    Q = list(map(int, input().split())) # 길이가 N인 Que
    Q.append(0)
    front = 0
    rear = N - 1
    for _ in range(M):
        # 맨 앞을 맨 뒤에 0 자리로 옮긴 다음 앞으로 밀기
        Q[N] = Q[front]
        for i in range(N):
            Q[i] = Q[i+1]
        Q[N] = 0

    ans = Q[0]

    print(f'#{tc} {ans}')