import sys
sys.stdin = open('input.txt')

num_dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
num_dict2 = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}

T = int(input())
for tc in range(1, T+1):
    t, N = map(str, input().split())
    N = int(N)
    # 배열 입력받기
    arr = list(map(str, input().split()))
    # 빈 배열 만들기
    c_arr = [0] * 10
    # 카운팅 배열 해줌
    for i in range(N):
        c_arr[num_dict[arr[i]]] += 1
    # 카운팅 배열에서 1씩 깎아주면서 dict에 있는 value 값 하나씩 프린트
    for k in range(len(c_arr)):
        print(t)
        while True:
            print(num_dict2[k], end=' ')
            c_arr[k] -= 1
            if c_arr[k] == 0:
                break