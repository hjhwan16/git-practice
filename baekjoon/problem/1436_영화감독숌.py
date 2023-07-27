# 완전 탐색
# 영화감독 숌

# 종말의 수: 6이 적어도 3개 이상 연속으로 들어가는 수
# 666, 1666, 2666, ....
# N번째 영화의 제목은 세상의 종말(N번째로 작은 종말의 수)

N = int(input())
cnt = 0
start = 1
while True:
    # 하나씩 증가하고 6이 연속으로 세번 나오며 카운트 하나 증가
    if '666' in str(start):
        cnt += 1
        start += 1    
        # 카운트와 N이 같아지는 순간
        if cnt == N:
            print(start-1)
            break 

    else: 
        start += 1

