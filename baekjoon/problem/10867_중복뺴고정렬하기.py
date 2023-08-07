# N개의 정수를 오름차순으로 정렬하는 프로그램을 작성,
# 같은 정수는 한 번만 출력

N = int(input())
arr = list(map(int, input().split()))
my_dict={}

for i in arr:
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1

key_arr = list(my_dict.keys())
key_arr.sort()

for k in key_arr:
    print(k, end=' ')
