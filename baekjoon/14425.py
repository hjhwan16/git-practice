# 문자열 집합

N, M = map(int, input().split())
my_set1 = set()
my_set2 = set()

cnt = 0

for i in range(N):
    my_set1.add(str(input()))
print(my_set1)
for i in range(M):
    word = str(input())
    # print({word} & my_set1)
    if (len({word} & my_set1)) == 1:
        cnt += 1

print(cnt)