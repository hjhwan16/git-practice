# 1학년 or 2학년 뉴비
# N학년 이하 + not 뉴비 -> OLDBIE
# 둘다 아니면 TLE

N, M = map(int, input().split())

if M == 1 or M == 2:
    print('NEWBIE!')
elif M <= N:
    print('OLDBIE!')
else:
    print('TLE!')