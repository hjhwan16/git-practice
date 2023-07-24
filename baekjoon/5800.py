# 성적 통계
K = int(input())
for i in range(K):
    num_list = [i+1]
    num_list += list(map(int, input().split()))
    # print(num_list)
    print(f'Class {num_list[0]}')
    score_list = num_list[2:]
    score_list.sort()
    gap_list = []
    for k in range(1, len(score_list)):
        # print(abs(score_list[k-1] - score_list[k]))
        gap_list.append(abs(score_list[k-1] - score_list[k]))
    #print(gap_list)
    print(f'Max {max(score_list)}, Min {min(score_list)}, Largest gap {max(gap_list)}')