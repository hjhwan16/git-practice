#  슈퍼마리오
#  완전 탐색

num_list = []
tot = 0

for i in range(10):
    a = int(input())
    
    if tot >= 100:
        tot += a
        pass
    else:
        tot += a
        num_list.append(tot)

if len(num_list) >= 2:
    big_number = num_list[-1]
    small_number = num_list[-2]

    if (abs(100 - big_number) > abs(100 - small_number)):
        print(small_number)
    else:
        print(big_number)

else:
    print(num_list[0])