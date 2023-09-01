# 체스판 다시 칠하기 / 20230901
'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

'''

N, M = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(input())
    arr.append(temp)
# print(arr)
# 8 by 8로 자르기
min_v = 65
for i in range(N-7):
    for j in range(M-7):
        check = []
        cnt1 = 0
        cnt2 = 0
        # print(i,j)
        for l in range(i, i+8):
            check.append(arr[l][j:j+8])
        # 이 지점을 기준으로 8 by 8 만들어 주면 됨
        # print(check)
        for k in range(64):
            r = k // 8
            c = k % 8
            # print('idx',k ,r,c)
            if (r+c) % 2 == 0:
                if check[r][c] == 'W':
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if check[r][c] == 'B':
                    cnt1 += 1
                else:
                    cnt2 += 1
            # print('cnt', cnt1, cnt2)
        if min_v > cnt1:
            min_v = cnt1
        if min_v > cnt2:
            min_v = cnt2
print(min_v)