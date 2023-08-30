N = int(input())        # 사진 틀의 갯수
M = int(input())        # 추천 횟수
arr = list(map(int, input().split())) # 추천정보
board = []
cnt_dict = {}
for i in range(M):  # M번 반복
    if arr[i] in board:
        # 틀 안에 있는 경우
        cnt_dict[arr[i]] += 1
        # print(board)
        # print(cnt_dict)
    else:
        # 틀 안에 없고 자리가 꽉 찬 경우
        # 제일 작은거 빼주기
        if len(board) == N:
            min_v = 1001
            min_i = 0
            for k in board:
                if min_v > cnt_dict[k]:
                    min_v = cnt_dict[k]
                    min_i = k
            board.remove(min_i)
            cnt_dict[min_i] = 0

            board.append(arr[i])
            if arr[i] not in cnt_dict.keys():
                cnt_dict[arr[i]] = 1
            else:
                cnt_dict[arr[i]] += 1
            # print(board)
            # print(cnt_dict)

        # 안에 없고 자리가 꽉 차지 않은 경우
        else:
            board.append(arr[i])
            cnt_dict[arr[i]] = 1
            # print(board)
            # print(cnt_dict)


board.sort()
print(*board)