# 인사성 밝은 곰곰이
# 오픈 채팅방에 새로운 분들이 입장하면 곰곰티콘으로 인사
# Enter 혹은 첫 채팅 = 곰곰티콘
# 총 곰곰티콘 사용 횟수는?

N = int(input())
cnt = 0
name_set = set()

for i in range(N):
    name = input()
    if name == 'ENTER':
        name_set = set() 
    elif name not in name_set:
        name_set.add(name)
        cnt += 1
    else:
        pass

print(cnt)