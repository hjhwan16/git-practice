# AC

def my_function(str_input, input_list):
    str_list = list(str_input)
    for i in range(len(str_list)):
        # 에러 반환 조건
        if  str_list.count('D') > len(input_list):
            return 'error'
        # 뒤집기 조건
        elif str_list[i] == 'R':
            input_list = input_list[::-1]
        # 버리기 조건
        elif str_list[i] == 'D':
            input_list = input_list[1:]
    return input_list

T = int(input())
for k in range(T):
    p = str(input())
    n = int(input())
    # 에러 조건
    try:
        my_list = list(map(int, input()[1:-1].split(',')))
        result = my_function(p, my_list)
        print(result)    
    except:
        print('error')
    