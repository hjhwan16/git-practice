# 소수 찾기
def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

min_num = int(input())
max_num = int(input())

prime_num_lst= []

for num in range(min_num, max_num + 1):
    if is_prime_num(num) == True:
        prime_num_lst.append(num)

if len(prime_num_lst) == 0:
    print(-1)
else:
    print(sum(prime_num_lst))
    print(min(prime_num_lst))

