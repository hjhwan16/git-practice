N, X = map(int, input().split())
arr = list(map(int, input().split()))
max_v = -1
for i in range(1, N):
    arr[i] += arr[i-1]
# print(arr)
#
for i in range(X-1, N):
    if i - X >= 0:
        temp = arr[i] - arr[i-X]
        # print(temp)
    else:
        temp = arr[i]
        # print(temp)


    if max_v < temp:
        cnt = 1
        max_v = temp
    elif max_v == temp:
        cnt += 1
if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(cnt)