import sys
sys.stdin = open('input.txt')

def backtracking(i, j, cnt, total):
    # 기저조건
    if cnt == 7:
        ans_set.add(total)
        return
    # 반복문
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            total += arr[ni][nj]
            backtracking(ni, nj, cnt+1, total)
            total = total[:-1]


T = int(input())
for tc in range(1, T+1):
    arr = []
    for _ in range(4):
        temp = list(map(str, input().split()))
        arr.append(temp)
    # print(arr)
    ans_set = set()
    for i in range(4):
        for j in range(4):
            backtracking(i, j, 0, '')

    ans = len(ans_set)
    print(f'#{tc} {ans}')