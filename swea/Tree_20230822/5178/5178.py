import sys
sys.stdin = open('input.txt')

def postorder(p, N):
    if p <= N:
        postorder(2*p, N)
        postorder(2*p + 1, N)
        if tree[p] == 0:
            if 2*p+1 <= N:
                tree[p] = tree[2*p] + tree[2*p+1]
            else:   # N이 2p 보다 큰 경우가 존재할 수 있기 때문에
                tree[p] = tree[2*p]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        arr = list(map(int, input().split()))
        tree[arr[0]] = arr[1]
    postorder(1, N)         # 마지막 지점 지정
    print(f'#{tc} {tree[L]}')