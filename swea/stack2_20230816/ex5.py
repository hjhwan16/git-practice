
# 부분집합의합 구하기 / 연습문제 / 백트래킹

def f(i, N, s, t): # s: i-1 원소까지의 합(포함된 원소의 합), t: 찾으려는 합
    global cnt
    cnt += 1
    if s == t:  # 찾았으면 그만
        print(bit, s)
        return
    elif s > t:  # 합이 t보다 커지는 경우
        return
    elif i == N:   #  원소가 없는 경우
        return
    else:
        bit[i] = 1 # A[i]가 포함이 되는 경우
        f(i+1, N, s+A[i], t)
        bit[i] = 0 # A[i]가 포함되지 않는 경우
        f(i+1, N, s, t)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는??
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 10) # 합이 10인 경우 가지치기
print(cnt)