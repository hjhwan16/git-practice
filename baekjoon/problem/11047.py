# 동전 0
cnt = 0
N, K = map(int, input().split())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
num_list = num_list[::-1]

for m in num_list:
    # if K == 0:
    #     print(cnt)
    #     break
    if K // m > 0:
        cnt += (K // m)
        K = K - (m * (K // m))
        print(K)
        if K == 0:
            print(cnt)
            break
