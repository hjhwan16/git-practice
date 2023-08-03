# 백준 11004 K번째 수
# 수 N개가 주어지고 이를 오름차순으로 정렬했을 때 K번째 있는 수는?

# N과 K 입력받기 / 내장함수 사용
# N, K = map(int, input().split())
# # arr 입력받고
# arr = list(map(int, input().split()))
# # 정렬 후 K번째 찾기
# arr.sort()
# print(arr[K-1])
# # 이 방법은 좀 느릴 듯? 되네?

# 버블 소트 사용하기 -> 시간 초과
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
# for i in range(N-1, 0, -1):
#     for j in range(0, i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#     if i == K-1:
#        print(arr[K-1])
 
# 선택정렬 사용하기
N, K = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(K):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]
print(arr[K-1])