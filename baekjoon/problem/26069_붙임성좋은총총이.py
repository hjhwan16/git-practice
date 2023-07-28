# 붙임성 좋은 총총이
# 사람들이 만난 기록이 시간 순서대로 N개 주어짐
# 무지개 댄스를 추지 않고 있던 사람이 무지개 댄스를 추고 있던 사람을 만나면 그 이후로는 무지개 댄스
# 총총이만 무지개 댄스를 추고 있음
# 마지막 기록 이후 무지개 댄스를 추는 사람은?

N = int(input())

name_list = ["ChongChong"]
dance_list = []

for i in range(N):
    A, B = input().split()
    # A만 댄스를 추고 있는 경우
    if (A in name_list) and (B not in name_list):
        name_list.append(B)
    # B만 댄스를 추고 있는 경우
    elif (B in name_list) and (A not in name_list):
        name_list.append(A)
    # 둘다 추고 있거나 둘 다 추고 있지 않거나
    else:
        pass
print(len(name_list))
    
    