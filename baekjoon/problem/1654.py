# 랜선 짜르기 # 이분 탐색 # 이진 탐색

# N개의 랜선을 만들어야 함.

# K개의 랜선을 갖고 있음

# 모두 N개의 같은 길이의 랜선으로 만들고 싶음

# 나머지는 버려야 함

# N개보다 많이 만드느 것도 N개를 만드는 것에 포함

# 만들 수 있는 최대 랜선의 길이는?

K, N = map(int, input().split())
# 갖고 있는 K개 랜선의 길이 배열
arr = []
for _ in range(K):
    arr.append(int(input()))
# ans 로 arr 안에 있는 값들의 몫을 더한 값이 N이 되어야 함
    
min_v = min(arr)
if K == N:
    ans = min_v
else:
    start_v = min_v // 2

    for num in range(start_v, 0, -1):
        temp = 0
        for lan in arr:
            temp += (lan // num)
        if temp == N:
            ans = num
            break


# N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력
print(ans)

