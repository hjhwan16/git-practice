import sys
sys.stdin = open('input.txt')

def f(i, N):
    global min_v

    if i == N:
        s = 0
        for k in range(N):
            s += arr[k][A[k]]
        # print(s)
        # s값 최소값 검증하기
        if s < min_v:
            min_v = s
        return
    else:
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    arr2 = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    ans = 0
    min_v = 10*N*N + 1
    A = [i for i in range(N)]
    f(0, N)

    print(f'#{tc} {min_v}')