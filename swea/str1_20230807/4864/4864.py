# 4864 / 20230807 / 스트링
# 문자열 비교
import sys
sys.stdin = open('input.txt')

T = int(input())
# # 바로 확인 하는 방법
# for tc in range(1, T+1):
#     str1 = str(input())
#     str2 = str(input())
#     ans = 0
#     if str1 in str2:
#         ans = 1
#
#     print(f'#{tc} {ans}')

# 다른 방법 도 있 을 듯? #브루트 포스
for tc in range(1, T+1):
    str1 = str(input()) # 4
    str2 = str(input()) # 10
    len1 = len(str1)
    len2 = len(str2)
    ans = 0

    for i in range(len2 - len1 + 1): #0,1,2,3,4,5,6
        # cnt 1로 초기화
        cnt = 1
        for k in range(len1):
            # 다르면 cnt를 0으로 만들어 버리고 break
            if str1[k] != str2[i+k]:
                cnt = 0
                break
        # 다 같으면 cnt 는 1로 남아 있고 이럴 경우 ans 에 1을 반환
        if cnt == 1:
            ans = 1
            break

    print(f'#{tc} {ans}')
