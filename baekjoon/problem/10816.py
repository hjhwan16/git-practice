# 이진탐색으로 풀어보기
# 숫자카드 2
# 상근이는 숫자 카드 N개를 갖고 있음
# 정수 M개가 주어질 때 이 수가 적혀있는 숫자카드를 상근이가 몇개 갖고 있는지?

# 상근이가 갖고 있는 카드의 개수
N = int(input())
# 상근이 카드 배열 
arr1 = list(map(int, input().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, input().plit()))

# 이진탐색 하면서 갯수 카운트?
for num in arr2:
    answer = 0
    start = 0
    end = N - 1
    while start <= end:
        center = (start + end) // 2
        if num == arr1[center]:
            