import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    heap[last] = n
    c = last
    p = c // 2
    last += 1
    while p > 0: # 부모가 있으면
        if heap[c] < heap[p]:   # 자식 노드의 값이 항상 크도록 바꿔줌
            heap[c], heap[p] = heap[p], heap[c]
            c = p   # 부모를 자손으로
            p = c // 2   # 뉴 부모 설정해주기
        else:
            break



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = [0] * (N + 1)
    last = 1
    arr = list(map(int, input().split()))
    # 입력받은 값들을 트리에 추가해주기
    for i in range(N):
        enq(arr[i])
    ans = 0
    # 조상 노드의 합을 더하기
    while True:
        N = N // 2
        ans += heap[N]
        if N == 1:
            break
    print(f'#{tc} {ans}')
