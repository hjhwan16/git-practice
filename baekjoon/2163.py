N, M = map(int, input().split())
count = 0
if N == 1 and M == 1:
    print(count)    
else:
    count = M * N - 1
    print(count)