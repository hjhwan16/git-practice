# 완전 탐색
# 분해합 # N의 가장 작은 생성자를 구해내는 프로그램을 작성

# 어떤 자연수 N이 있을 때 N의 분해합은 N과 N을 이루는 각 자리수의 합
# 어떤 자연수 M의 분해합이 N인 경우 M을 N의 생성자라고 함.
# 245의 분해합은 245+2+4+5 = 256
# 245는 256의 생성자
# 256의 생성자: 245
# 생성자가 없을 수 도 있음
# 생성자가 여러개일 수 도 있음 

N = int(input())
num_list = []

for i in range(1, N+1):
    part_sum = 0
    for k in range(len(str(i))):
        part_sum += int(str(i)[k])
    num = i + part_sum
    if num == N:
        num_list.append(i)
        # print(num_list)

if len(num_list) == 0:
    print(0)
else:
    print(min(num_list))

    

        
            