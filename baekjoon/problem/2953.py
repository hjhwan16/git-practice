# 나는 요리사다
name_lst = []
score_lst=[]
for i in range(5):
    s1, s2, s3, s4 = map(int, input().split())
    name_lst.append(i+1)
    score_lst.append(s1 + s2 + s3 + s4)

winner = name_lst[score_lst.index(max(score_lst))]
print(winner, max(score_lst))