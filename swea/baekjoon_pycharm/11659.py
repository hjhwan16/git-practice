N ,M = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(M):
    i, j = map(int, input().split())
    temp = 0
    for k in range(i-1, j):
        temp += arr[k]
    print(temp)

'''
5 3
5 4 3 2 1
1 3
2 4
5 5

'''