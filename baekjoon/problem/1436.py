# 1로만들기 / 1463

N = int(input())
dp = [0] * (N + 1)
cnt = 0
while True:
    if N % 3 == 0:
        cnt += 1
        N = int(N / 3)
        if N == 1:
            print(cnt)
            break
    elif N % 2 == 0:
        cnt += 1
        N = int(N / 2)
        if N == 1:
            print(cnt)
            break
    else:
        cnt += 1
        N = N - 1
        if N == 1:
            print(cnt)
            break
