import sys
sys.stdin = open('input.txt')

N = int(input())
paper_lst = []
for _ in range(N):
    x, y, w, h = map(int, input().split())
    temp_set = set()
    for i in range(x, x+w):
        for j in range(y, y+h):
            temp_set.add((i, j))
    if not paper_lst:
        paper_lst.append(temp_set)
    else:
        for i in range(len(paper_lst)):
            paper_lst[i] -= temp_set
        paper_lst.append(temp_set)
for i in paper_lst:
    print(len(i))