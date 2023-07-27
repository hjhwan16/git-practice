# 점수 집계
T = int(input())
for i in range(T):
    score_list = []
    score_list = list(map(int, input().split()))
    score_list.sort()
    score_list = score_list[1:4]
    #print(score_list)
    diff = max(score_list) - min(score_list)
    if diff >= 4:
        print("KIN")
    else:
        print(sum(score_list))