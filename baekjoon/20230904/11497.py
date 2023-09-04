# 통나무 건너뛰기 / 20230904

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)
    final_arr = []

    for i in range(N):
        temp = arr.pop()
        if i%2 == 0:
            final_arr = final_arr + [temp]
        else:
            final_arr = [temp] + final_arr
    final_arr += [final_arr[0]]
    # print(final_arr)
    max_v = -1
    for i in range(N):
        temp = final_arr[i+1] - final_arr[i]
        if temp < 0:
            temp *= -1
        if max_v < temp:
            max_v = temp
    print(max_v)

'''
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6

'''