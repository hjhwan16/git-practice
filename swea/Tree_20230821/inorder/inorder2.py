import sys
sys.stdin = open('input.txt')

def inorder(p, N):      # N완전 이진트리의 마지막 정ㅈ머
    if p <= N:
        inorder(p*2, N)
        print(tree[p], end='')
        inorder(2*p+1, N)


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
    # 중위 순회
    inorder(1, N)
    print()# root = 1