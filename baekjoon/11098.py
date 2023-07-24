testcase = int(input())
for case in range(testcase):
    player_num = int(input())
    cost_lst=[]
    name_lst=[]
    for player in range(player_num):
        cost, name = map(str, input().split())
        cost_lst.append(int(cost))
        name_lst.append(name)
    print(name_lst[cost_lst.index(max(cost_lst))])