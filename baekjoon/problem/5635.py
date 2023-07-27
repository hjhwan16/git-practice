num = int(input())
birthdays = []
for i in range(num):
    temp = []
    name, day, month, year = map(str, input().split())
    temp = [name, int(year), int(month), int(day)]
    birthdays.append(temp)

# 이중 리스트 정렬 하기
birthdays.sort(key = lambda x: (x[1], x[2], x[3]))
print(birthdays[-1][0])
print(birthdays[0][0])
