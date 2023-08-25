import sys
sys.stdin = open('input.txt')

bingo = []
for _ in range(5):
    temp = list(map(int, input().split()))
    bingo.append(temp)

numbers = []
for _ in range(5):
    temp = list(map(int, input().split()))
    numbers += temp


def is_Bingo(bingo):
    # 가로
    cnt = 0
    for i in range(5):
        if bingo[i] == [0]*5:
            cnt += 1

    for j in range(5):
        temp = []
        for i in range(5):
            temp.append(bingo[i][j])
        if temp == [0]*5:
            cnt += 1
    temp1 = []
    temp2 = []
    for i in range(5):
        temp1.append(bingo[i][i])
        temp2.append(bingo[i][4-i])
    if temp1 == [0]*5:
        cnt += 1
    if temp2 == [0]*5:
        cnt += 1
    return cnt

ans = 0

for number in numbers:
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                bingo[i][j] = 0
                ans += 1
    if is_Bingo(bingo) >= 3:
        break
print(ans)
