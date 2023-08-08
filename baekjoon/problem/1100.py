# 하얀 칸 / 20230808

ans = 0
# 2차원 배열 받기
arr = []
for _ in range(8):
    temp = list(str(input()))
    arr.append(temp)

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            if arr[i][j] == 'F':
                ans += 1
        elif i % 2 == 1 and j % 2 == 1:
            if arr[i][j] == 'F':
                ans += 1 

print(ans)