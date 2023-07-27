# 소수 찾기
def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))
prime_num_lst= []

for num in numbers:
    if is_prime_num(num) == True:
        prime_num_lst.append(num)

print(len(prime_num_lst))
