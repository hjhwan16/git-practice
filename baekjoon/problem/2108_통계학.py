# 통계학
# N개의 수가 주어졌을 때
# 1. 산술평균
# 2. 중앙값
# 3. 최빈값
# 4. 범위

num_list = []
N = int(input())
for i in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort()
# 산술평균
print(int(sum(num_list)/len(num_list)))
# 중앙값
print(num_list[(len(num_list)-1)/2])
# 최빈값 어떻게 하는지 모르겠다
new_list = [0] * (max(num_list) - min(num_list))

print()
# 범위
print(max(num_list) - min(num_list))