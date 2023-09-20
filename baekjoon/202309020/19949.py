# 백트래킹 문제
def backtracking(cnt):
    global ans
    # 기저조건
    if cnt == 10:
        s = 0
        for j in range(10):
            if path[j] == arr[j]:
                s += 1
        if s >= 5:
            ans += 1
        return
    # 반복조건
    for i in range(5):
        if cnt > 1 and path[cnt-2] == path[cnt-1] == ans_list[i]:
            continue
        path.append(ans_list[i])
        backtracking(cnt+1)
        path.pop()



arr = list(map(int, input().split()))
N = len(arr)
ans_list = [1, 2, 3, 4, 5]
path = []
ans = 0
backtracking(0)
print(ans)