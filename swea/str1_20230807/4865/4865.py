# 4865 / 20230807 / 스트링
import sys
sys.stdin = open('input.txt')

# str1과 str2가 주어짐
# 문자열 str1에 str2가 몇개씩 들어있는지 찾고, 그 중 가장 많은 글자의 개수를 출력하는 프로그램


T = int(input())
for tc in range(1, T+1):
    ans = 0
    str1 = str(input())
    str2 = str(input())
    len1 = len(str1)
    len2 = len(str2)
    my_dict = {}
    # str1에 있는 문자열을 key로 value를 0으로 하는 딕셔너리 생성
    for i in range(len1):
        if str1[i] not in my_dict.keys():
            my_dict[str1[i]] = 0
        else:
            pass
    # str2에 있는 문자열이 dict에 있다면 value를 하나씩 키워줌
    for k in range(len2):
        if str2[k] in my_dict.keys():
            my_dict[str2[k]] += 1
        else:
            pass
    # dict value 값중에서 최대값을 뽑아 줌

    arr = list(my_dict.values())
    max_v = arr[0]
    for num in arr:
        if max_v < num:
            max_v = num
    ans = max_v

    print(f'#{tc} {ans}')