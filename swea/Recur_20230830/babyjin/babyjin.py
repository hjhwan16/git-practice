import sys
sys.stdin = open('input.txt')

def f(S, K, N, p_in):
    global ans
    if S == K:
        # print(pp)
        # triples 확인
        if pp[0] == pp[1] and pp[1] == pp[2]:
            # print('triple')
            ans = 1
        # run 확인
        elif pp[0] - 1 in pp and pp[0] - 2 in pp:
            ans = 1
        elif pp[0] - 1 in pp and pp[0] + 1 in pp:
            ans = 1
        elif pp[0] + 1 in pp and pp[0] + 2 in pp:
            ans = 1

    else:
        for j in range(N):
            if used[j] == 0:
                pp[S] = p_in[j]
                used[j] = 1
                f(S+1, K, N, p_in)
                used[j] = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    result = 0
    for i in range(len(arr)//2):
        p1.append(arr[2*i])
        p2.append(arr[2*i+1])
        if len(p1) >= 3:
            # print(p1, p2)
            ans = 0
            used = [0] * (i+1)
            pp = [0] * 3
            result1 = f(0, 3, i+1, p1)

            ans = 0
            used = [0] * (i + 1)
            pp = [0] * 3
            result2 = f(0, 3, i + 1, p2)
            # print(result1, result2)
            if result1:
                result = 1
                break
            if result2:
                result = 2
                break

        # 0시작, 집합 n, i+1: 총 카드갯수
        if result != 0:
            break
    print(f'#{tc} {result}')
