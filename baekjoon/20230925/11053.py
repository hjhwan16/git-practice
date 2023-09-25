# 백 트래킹
def backtracking():
    global max_len

    if path and path[-1] == max_v:
        if max_len < len(path):
            max_len = len(path)
        return

    # 조건 반복문
    for num in arr:
        if num in path:
            continue
        path.append(num)
        backtracking()
        path.pop()


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_v = max(arr)
arr = set(arr)
max_len = -1


print(len(arr))
