import sys
sys.stdin = open('input.txt')

# n이 밖에 있는 수. ans가 node에 적히는 수
def inorder(n):
    global ans
    if n:
        inorder(ch1[n])
        ans += 1
        lst[n] = ans
        inorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = N
    E = V - 1
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    lst = [0] * (V+1)
    cnt = 2

    for i in range(1, N+1):
        if ch1[i] == 0:
            ch1[i] = cnt
            cnt += 1
            if cnt == N+1:
                break
        if ch2[i] == 0:
            ch2[i] = cnt
            cnt += 1
            if cnt == N+1:
                break
    ans = 0
    inorder(1)
    ans1 = lst[1]
    ans2 = lst[N//2]
    print(f'#{tc} {ans1} {ans2}')

