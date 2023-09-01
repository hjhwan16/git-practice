import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1 << N):     # 2의 N제곱
        s = 0                   # 부분집합의 합
        for j in range(N):      # j번 비트 검사
            if i & (1 << j) != 0:    # j번 비트가 0이 아니면
                s += arr[j]     # 더해주기
        if s == K:
            cnt += 1

    print(f'#{tc} {cnt}')

'''
비트 연산자
&: 두개의 비트가 모두 1일 때 1을 반환하는 연산
<<: 비트를 왼쪽으로 이동하는 shift 연산 
'''