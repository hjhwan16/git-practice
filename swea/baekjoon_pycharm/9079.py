'''
3
H T T
H T T
T H H
T H H
H H H
H H H
H H H
H T H
H H H

'''
from copy import deepcopy

def isDone(arr):
    cnt_h = 0
    cnt_t = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 'H':
                cnt_h += 1
            if arr[i][j] == 'T':
                cnt_t += 1
    if cnt_t == 9 or cnt_h == 9:
        return True
    else:
        return False


def subset(i, N ,a):
    global min_v
    if i == N:
        temp = 0
        temp_lst = []
        for j in range(N):
            if bit[j]:
                temp_lst.append(A[j])
        # print(temp_lst)
        # print(arr)
        arr = deepcopy(a)
        # print(temp_lst)
        for k in temp_lst:
            # print(arr)
            if k == 0:
                for l in range(3):
                    if arr[0][l] == 'H':
                        arr[0][l] = 'T'
                    else:
                        arr[0][l] = 'H'
                temp += 1
            elif k == 1:
                for l in range(3):
                    if arr[1][l] == 'H':
                        arr[1][l] = 'T'
                    else:
                        arr[1][l] = 'H'
                temp += 1
            elif k == 2:
                for l in range(3):
                    if arr[2][l] == 'H':
                        arr[2][l] = 'T'
                    else:
                        arr[2][l] = 'H'

                temp += 1
            elif k == 3:
                for l in range(3):
                    if arr[l][0] == 'H':
                        arr[l][0] = 'T'
                    else:
                        arr[l][0] = 'H'
                temp += 1
            elif k == 4:
                for l in range(3):
                    if arr[l][1] == 'H':
                        arr[l][1] = 'T'
                    else:
                        arr[l][1] = 'H'

                temp += 1
            elif k == 5:
                for l in range(3):
                    if arr[l][2] == 'H':
                        arr[l][2] = 'T'
                    else:
                        arr[l][2] = 'H'
                temp += 1
            elif k == 6:
                for l in range(3):
                    if arr[l][l] == 'H':
                        arr[l][l] = 'T'
                    else:
                        arr[l][l] = 'H'
                temp += 1
            elif k == 7:
                for l in range(3):
                    if arr[l][2-l] == 'H':
                        arr[l][2-l] = 'T'
                    else:
                        arr[l][2-l] = 'H'
                temp += 1
            if isDone(arr):
                # print(temp)
                if min_v > temp:
                    min_v = temp
                break

    else:
        bit[i] = 1
        subset(i+1, N, a)
        bit[i] = 0
        subset(i+1, N, a)


T = int(input())
for tc in range(1, T+1):
    arr = []
    for _ in range(3):
        temp = list(input().split())
        arr.append(temp)
    # print(arr)
    min_v = 9
    A = [x for x in range(8)]
    # print(A)
    bit = [0] * 8
    if isDone(arr):
        print(0)
    else:
        subset(0, 8, arr)
        if min_v == 9:
            print(-1)
        else:
            print(min_v)
