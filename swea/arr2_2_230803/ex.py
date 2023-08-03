# 할 수 있다. / 20230803

arr = ['Fish', 'And', 'Chips']
# N = len(arr) # 배열의 길이
# #
# # # arr의 부분집합에 대한 모든 경우의 수
# for i in range(1 << N):
#     for j in range(N):
#         if i & (1 << j):
#             print(arr[j], end=' ')
#     print()
'''

Fish
And
Fish And
Chips
Fish Chips
And Chips
Fish And Chips
'''

# 1 << 2의 이미
N = 3
print(1 << N)  # 8

'''
2진수 | 10진수 | shift 횟수 |
--------------------------
0001 | 1      |   0
0010 | 2      |   1
0100 | 4      |   2
1000 | 8      |   3
--------------------------
'''

# 3개 원소를 갖고 만들 수 있는 부분집합의 모든 경우의 수 2 ** 3

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()

# i = 3번째 경우

# if 문을 통과하기 위해서는
# i값 부터 오른쪽으로 n번째 비트값이 1이어야 함.
# j = 0, 1, 2

# 3 & (1 << 0) -> 011
'''
--------------------------
3      |   0     |   
And    |   1     |   
result |   1     |   
--------------------------
'''

# 3 & (1 << 1) ->
# 3 & (1 << 2) ->

