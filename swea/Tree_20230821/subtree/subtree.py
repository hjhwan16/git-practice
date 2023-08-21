import sys
sys.stdin = open('input.txt')

def preorder(n):
    global ans
    if n:
        ans += 1
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())        # E: 간선의 갯수, N: 루트 노드,
    arr = list(map(int, input().split()))
    # 부모를 인덱스로 자식을 저장
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    for i in range(E):
        p, c = arr[i*2], arr[2*i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    ans = 0
    preorder(N)
    print(f'#{tc} {ans}')