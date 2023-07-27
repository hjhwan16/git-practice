# 0의 갯수
T = int(input())
for i in range(T):
    tot = 0
    N, M = map(int, input().split())
    for i in range(N, M+1):
        tot += str(i).count('0')
    print(tot)