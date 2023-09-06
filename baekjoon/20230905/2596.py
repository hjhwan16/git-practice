# 비밀편지 / 20230905
# 비트연산자 하나씩 바꾸고 확인하기
pwd_dict = {'000000':'A', '001111':'B', '010011':'C', '011100':'D', '100110':'E', '101001':'F', '110101':'G', '111010':'H'}
N = int(input())
num = str(input())
arr = []
flag = True
for i in range(N):
    arr.append(num[i*6:i*6 + 6])
# print(arr)
ans = ''
for i in range(N):
    if arr[i][:6] in pwd_dict.keys():
        ans += pwd_dict[arr[i][:6]]
        # print(ans)
    else: # i에서 하나의 숫자를 바꾼게 dict key에 있다면 temp_arr에 추가 temp_arr의 길이가 1이면 진행 아니면 break
        temp_set = set()
        for j in range(6):
            if arr[i][j] == '0':
                temp = arr[i][:j] + '1' + arr[i][j+1:]
            else:
                temp = arr[i][:j] + '0' + arr[i][j+1:]
            if temp[:6] in pwd_dict.keys():
                temp_set.add(pwd_dict[temp[:6]])
        # print(temp_set, len(temp_set))
        if len(temp_set) == 1:
            ans += list(temp_set)[0]
        else:
            flag = False
            ans2 = i+1
            break
if flag:
    print(ans)
else:
    print(ans2)
