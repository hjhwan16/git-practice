# 콘테스트
w_list = []
k_list = []

for w in range(10):
    score = int(input())
    w_list.append(score)

for k in range(10):
    score = int(input())
    k_list.append(score)

w_list.sort()
k_list.sort()

print(sum(w_list[-3:]), sum(k_list[-3:]))