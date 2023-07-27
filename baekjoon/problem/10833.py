school_num = int(input())
total = 0
for i in range(school_num):
    stu, app = map(int, input().split())
    total += app % stu
print(total)