# 진법 변환
tot = 0
dict_alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U':30, 'V': 31, 'W': 32, 'X':33, 'Y': 34, 'Z':35}

N, B = map(str, input().split())
num_list = list(N)

for i in range(len(num_list)):
    if num_list[i].isalpha():
        num_list[i] = dict_alpha[num_list[i]]

# print(num_list)
num_list = num_list[::-1]
# print(num_list)

for k in range(len(num_list)):
    tot += int(num_list[k]) * (int(B)**(k))

print(tot)