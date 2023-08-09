import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

# 주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

# for문 사용
# T = 10
# for tc in range(1, T+1):
#     tc_in = int(input())
#     pattern = str(input())
#     target = str(input())
#     ans = 0
#     n = len(pattern)
#     m = len(target)
#     for i in range(m-n+1):
#         temp = 0
#         for k in range(n):
#             if pattern[k] != target[i+k]:
#                 temp = 1
#                 break
#         if temp == 0:
#             ans += 1
#
#     print(f'#{tc} {ans}')

# while문 사용
T = 10
for tc in range(1, T+1):
    tc_in = int(input())
    pattern = str(input())
    target = str(input())
    ans = 0
    n = len(pattern)
    m = len(target)
    i = 0 #target의 idx
    j = 0 #pattern의 idx

    while i < m:
        # 다른 곳을 만남
        if target[i] != pattern[j]:
            # 타겟은 뒤로 돌아가기
            i = i - j
            # 패턴은 맨 앞으로
            j = -1
        i = i + 1
        j = j + 1
        if j == n:
            ans += 1
            j = 0

    print(f'#{tc} {ans}')