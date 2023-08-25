import sys
sys.stdin = open('input.txt')

# 후위계산식으로 뽑아준 다음 계산의 결과를 p에 다시 반환
def postorder(p):
    if p:
        postorder(ch1[p])
        postorder(ch2[p])
        if tree[p] in '*-+/':
            if tree[p] == '*':
                tree[p] = int(tree[ch1[p]]) * int(tree[ch2[p]])
            elif tree[p] == '-':
                tree[p] = int(tree[ch1[p]]) - int(tree[ch2[p]])
            elif tree[p] == '+':
                tree[p] = int(tree[ch1[p]]) + int(tree[ch2[p]])
            elif tree[p] == '/':
                tree[p] = int(tree[ch1[p]]) // int(tree[ch2[p]])




T = 10
for tc in range(1, T+1):
    N = int(input())        # 정점의 개수
    tree = [0] * (N+1)      # tree
    ch1 = [0] * (N+1)       # 왼쪽 자식
    ch2 = [0] * (N+1)       # 오른쪽 자식
    for i in range(N):
        arr = list(input().split())
        tree[i+1] = arr[1]
        if len(arr) > 2:
            ch1[i+1] = int(arr[2])
            ch2[i+1] = int(arr[3])
    ans = 0
    postorder(1)

    print(f'#{tc} {tree[1]}')