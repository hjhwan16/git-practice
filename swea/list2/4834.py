# 숫자카드
import sys
sys.stdin = open('input.txt')
# 숫자카드
# 0에서 9까지 숫자가 적힌 N장의 카드가 주어짐.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력

import sys

sys.stdin = open('input.txt')
# 숫자카드
# 0에서 9까지 숫자가 적힌 N장의 카드가 주어짐.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 카드 장수
    arr = list(map(int, input()))  # 카드 인풋받기
    count_list = [0] * 10  # 빈 리스트 만들기
    # arr을 돌며 카드 한장 나올때 마다 count_list 하나씩 올리기
    for i in arr:
        count_list[i] += 1

    max_v = count_list[0]  # 최댓값 임의 지정
    mx_idx = 0  # 최댓값 인덱스 임의 지정
    # 최댓값 찾기
    for k in range(len(count_list)):
        if count_list[k] >= max_v:
            max_v = count_list[k]
            max_idx = k

    print(f'#{tc} {max_idx} {max_v}')