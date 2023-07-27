day = int(input())
car_lst=list(map(int, input().split()))
#print(car_lst)
print(car_lst.count(day % 10))