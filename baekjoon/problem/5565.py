total = int(input())
book_lst = []
for i in range(9):
    price = int(input())
    book_lst.append(price)
print(total-sum(book_lst))