# 올림픽 / 20230906
N, K = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
arr.append([0,0,0,0])
arr.sort(reverse=True, key=lambda x:(x[1],x[2],x[3]))
rank_lst = []
rank = 1
cnt = 1

for i in range(N):
    if arr[i][1:] == arr[i+1][1:]:
        if arr[i][0] == K:
            print(rank)
            break
        cnt += 1
        # print(cnt)
        rank_lst.append(rank)
        continue
    else:
        if arr[i][0] == K:
            print(rank)
        rank_lst.append(rank)
        rank += cnt
        cnt = 1

# print(rank_lst)
'''
5 4
1 3 0 0
2 3 0 0
3 2 0 0
4 1 0 0
5 2 0 0

'''
