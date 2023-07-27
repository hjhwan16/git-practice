# 숫자의 개수
digit =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
A = int(input())
B = int(input())
C = int(input())
num = str(A * B * C)

for i in digit:
    print(num.count(i))