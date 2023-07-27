# 수 찾기
N = int(input())
set1 = set(list(map(int, input().split())))
M = int(input())
list1 = list(map(int, input().split()))

for i in list1:
    set2 = {i}
    print(len(set1 & set2))