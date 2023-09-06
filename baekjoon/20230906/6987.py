arr = []
for _ in range(4):
    temp = list(map(int, input().split()))
    arr.append(temp)
# print(arr)
ans = [1] * 4
draw_list = [0] * 6
score_list = [0] * 6
for i in range(4):
    group_list = []
    win_cnt = 0
    lose_cnt = 0
    draw_cnt = 0
    for k in range(6):
        group = arr[i][3*k:(k+1)*3]
        group_list.append(group)
        win_cnt += arr[i][3*k]
        draw_cnt += arr[i][3*k+1]
        lose_cnt += arr[i][3*k+2]
        draw_list[k] = arr[i][3*k+1]
        score = sum(arr[i][3*k:3*(k+1)])
        score_list[k] = score
    # print(1, draw_list)
    for j in range(6):
        if draw_list[j] > 0:
            for w in range(6):
                if j == w:
                    continue
                elif draw_list[w] == 0:
                    continue
                elif draw_list[w] == draw_list[j]:
                    draw_list[w], draw_list[j] = 0, 0
                    break
                elif draw_list[w] < draw_list[j]:
                    draw_list[j], draw_list[w] = draw_list[j]-draw_list[w], 0
                else:
                    draw_list[j], draw_list[w] = 0, draw_list[w] - draw_list[j]
        else:
            pass
    # print(score_list)
    # print(2, draw_list)
    # print(win_cnt, lose_cnt, draw_cnt)
    # print(win_cnt + lose_cnt + draw_cnt)
    if win_cnt + lose_cnt + draw_cnt != 30:
        # print(i, 30)
        ans[i] = 0
    elif win_cnt != lose_cnt:
        # print(i)
        ans[i] = 0
    elif draw_list != [0] * 6:
        ans[i] = 0
    elif score_list != [5] * 6:
        ans[i] = 0

    # print(group_list)
print(*ans)
