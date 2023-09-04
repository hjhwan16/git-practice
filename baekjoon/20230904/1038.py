# 감소하는 수 / 20230904
import math
from itertools import combinations
cnt_list = [0] * 10

for i in range(10):
    temp = 0
    for j in range(10):
        temp += math.comb(j, i)
    if i != 0:
        cnt_list[i] = cnt_list[i-1] + temp
    else:
        cnt_list[i] = temp - 1
# print(cnt_list)

N = int(input())
if N > 1022:
    print(-1)
else:
    for i in range(10):
        if N <= cnt_list[i]:
            # print(i)
            if i >= 1:
                # i+1 자릿수의 (N-cnt_lst[i-1])번째 숫자
                cnt = 0
                for j in range(i, 10):
                    flag = False
                    arr = []
                    for k in range(j):
                        arr.append(k)
                    ncr = list(combinations(arr, i))
                    ncr.sort()
                    # print(ncr)
                    ncr_list = []
                    for g in ncr:
                        temp = ''
                        g = g[::-1]
                        for m in g:
                            temp += str(m)
                        ncr_list.append(temp)
                    ncr_list.sort()
                    # print(ncr_list)
                    for l in ncr_list:
                        cnt += 1
                        # print(l, cnt)
                        # print(N - cnt_list[i - 1] + 1)
                        if cnt == (N - cnt_list[i - 1]):
                            ans = str(j)
                            for i in l:
                                ans += i
                            print(ans)
                            flag = True
                            break
                    if flag:
                        break
            else:
                print(N)
            break
        else:
            continue
