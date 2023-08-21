# 참가자 N명은 원을 이뤄 앉음
# 1부터 N까지 번호가 적혀있는 티셔츠를 입음
# 1단계 백준이는 어떤 참가자의 앞에 하나
# 시계방향으로 다음 사람이게 이동하여 둘
# 1단계 1 2단계 8 3단계 27 t단계 t^3까지 외침
# 각 단계가 ㄱ끝난 후 백준이가 앞에 있는 사람은 제외

N = int(input())
arr = [i for i in range(1, N+1)]
front = 0
cnt = 1
while True:
    if N == 1: # 남은 사람의 수
        break
    else:
        front = (front + cnt**3 - 1) % N
        arr.pop(front)
        cnt += 1
        N -= 1

for i in arr:
    print(i)

