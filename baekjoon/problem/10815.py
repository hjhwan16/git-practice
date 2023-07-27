# 숫자카드
N = int(input())
card_set = set(map(int, input().split()))
M = int(input())
new_list = list(map(int, input().split()))

# print(set(new_list))
# print({9})
for i in new_list:
    print(len((card_set) & {i}), end=' ')