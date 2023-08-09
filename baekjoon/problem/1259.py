# 팰린드롬수

# 회문

# 20230809

while True:
    num = str(input())
    if num == '0':
        break
    N = len(num)
    answer = 'yes'
    for i in range(N//2):
        if num[i] != num[N-i-1]:
            answer = 'no'
            break
        else:
            pass
    print(answer)