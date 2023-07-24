# 점수 계산
score_list = []
idx_list = []
top_list = []
for i in range(8):
    score = int(input())
    score_list.append([i+1, score])

# score 기준으로 내림차순 정렬하기
score_list.sort(key = lambda x: x[1], reverse = True)
# print(score_list)

for k in range(5):
    top_list.append(score_list[k][1])
    idx_list.append(score_list[k][0])

idx_list.sort()

print(sum(top_list))

for m in idx_list:
    print(m, end=' ')

