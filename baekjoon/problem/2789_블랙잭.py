# 완전 탐색
# 블랙잭
# 세 장의 카드를 고르는 모든 경우를 고려하는 문제

# N장의 카드 중에서 3장의 카드를 골라 그 합이 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 함. -> 이를 출력

N, M = map(int, input().split()) # 전체 카드 N장 중 M장을 뽑아야함
card_list = list(map(int, input().split()))

tot_list = []

for i in range(N):
    for j in range(N):
        for k in range(N):
            if (i == j) or (i == k) or (j == k):
                pass
            else:
                tot = card_list[i] + card_list[j] + card_list[k]
                if tot > M:
                    pass
                else:
                    tot_list.append(tot)

print(max(tot_list))
