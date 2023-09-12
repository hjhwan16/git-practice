import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_v = 0
for i in range(1, N-2):
    temp = arr[i:]
    # print(i, temp)
    for j in range(N-1-i):
        temp[j] -= i
    # print(i, temp, arr)
    for k in range(N-1-i):
        total = arr[i]
        total += (arr[i]+temp[k])
        # print(i+temp[k], total)
        cnt = 2
        for l in range(k+1, N-1-i):
            if temp[l] == temp[k]*cnt:
                cnt += 1
                # print(arr[i], temp[k], (temp[l]+arr[i]))
                total += (temp[l]+arr[i])
                # print('check', total)
        if cnt >= 3:
            # print(total)
            if max_v < total:
                max_v = total
print(max_v)





