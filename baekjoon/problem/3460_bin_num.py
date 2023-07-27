#이진수
T = int(input())
for i in range(T):
    n = int(input())
    # print(bin(n)) # 0b1100
    bin_num = bin(n)[2:][::-1]
    #print(bin_num) # 1100
    for k in range(len(bin_num)):
        if bin_num[k] == '1': #2진수 이기 때문에 int가 아닌 str로
            print(k, end=' ')
    print()