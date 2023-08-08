# # 수 찾기
# N = int(input())
# set1 = set(list(map(int, input().split())))
# M = int(input())
# list1 = list(map(int, input().split()))

# for i in list1:
#     set2 = {i}
#     print(len(set1 & set2))

# 이진탐색으로 풀기
N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))


for i in arr2:
    answer = 0 # answer 초기화
    # 이진탐색으로 찾기
    start = 0
    end = N - 1
    while start <= end:
        center = (start+end) // 2
        # 찾으면 answer를 1로 반환
        if i == arr1[center]:
            answer = 1
            break
        elif i < arr1[center]:
            end = center - 1
        elif i > arr1[center]:
            start = center + 1
    print(answer)