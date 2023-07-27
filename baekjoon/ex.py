arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]

count = [0] * (max(arr) + 1)

for num in arr:
    count[num] += 1

print(count)