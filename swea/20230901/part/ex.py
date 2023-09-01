A = [1, 2, 3, 4, 5]
N = 5
K = 3

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j) != 0:
            print(A[j], end= ' ')
    print()
    
# K개의 부분집합을 구하는 법

for i in range(1 << N):
    cnt = 0
    temp = []
    for j in range(N):
        if i & (1 << j) != 0:
            cnt += 1
            temp.append(A[j])
    if cnt == K:
        print(temp)