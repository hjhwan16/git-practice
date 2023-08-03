import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 정수의 개수 N과 구간의 개수 M
    arr = list(map(int, input().split())) # 정수의 개수 N개
    ans = 0
    max_v = 1 * M # 최댓값 지정
    min_v = 10000 * M # 최솟값 지정

    for i in range(N - M + 1): # 구간별로 돌면서 값을 합해줌.
        tot = 0
        for k in range(M):
            tot += arr[i+k]

        if tot > max_v: # 최댓값 변환
            max_v = tot

        if tot < min_v: # 최솟값 변환
            min_v = tot

    ans = max_v - min_v
    print(f'#{tc} {ans}')