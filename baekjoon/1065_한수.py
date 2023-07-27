# 한수
# 완전 탐색
# 어떤 양의 정수 x의 각자리가 등차수열일 이룬다면 그 수를 한수
# 연속된 두개의 수의 차이가 일정한 수열을 의미
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램 작성

N = int(input())
cnt = 0

for i in range(1, N+1): # 1부터 N까지 차레로 도입
    temp = set()
    if i < 10:
        cnt += 1
    else:
        for k in range(len(str(i)) - 1): #ㅑ = 10이 들어온 경우 0,1
            temp.add(int(str(i)[k]) - int(str(i)[k + 1]))
        if len(temp) == 1:
            cnt += 1

print(cnt)



