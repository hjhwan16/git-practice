def f(i, N, K):
    global arr
    if i == K:        # 순열 완성
        print(p)
        return
    else:             # card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0

card = list(map(int, input()))
N = 5   # N개의 숫자에서
K = 3   # K개를 골라 만드는 순열
used = [0] * 5      # 이미 사용한 카드인지 표시
p = [0] * 3
arr = []
f(0, 5, 3)
print(arr)