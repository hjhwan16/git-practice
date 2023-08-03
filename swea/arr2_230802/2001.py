import sys
sys.stdin = open('input.txt')
# extra / 2001 / 파리퇴치
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 죽은 파리의 개수를 구하라.

# N은 5 이상 15 이하이다.
# M은 2 이상 N 이하이다.
# 각 영역의 파리 갯수는 30이하이다.

# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N by N 배열 입력받기
    ans = 0
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # M크기의 파리채로 내려치기
    for i in range(N):
        for j in range(N):
            tot = 0
            for k in range(M):
                for l in range(M):
                    # map 밖을 나가면 안함
                    if i+k >= N or j+l >= N:
                        continue
                    else:
                        tot += arr[i+k][j+l]
            if ans < tot:
                ans = tot

    print(f'#{tc} {ans}')