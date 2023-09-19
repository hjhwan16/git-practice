from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    combi = list(combinations(sorted(arr[1:]), 6))
    for i in combi:
        print(*i)
    print()

'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

'''