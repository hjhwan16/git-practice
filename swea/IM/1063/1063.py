import sys
sys.stdin = open('input.txt')

board_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
move_dict = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0], 'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}
king, stone, N = input().split()
ki, kj = 9 - int(king[1]), board_dict[king[0]]
si, sj = 9 - int(stone[1]), board_dict[stone[0]]

print(ki, kj)
print(si, sj)
print()

for _ in range(int(N)):
    cmd = str(input())
    nki = ki + move_dict[cmd][0]
    nkj = kj + move_dict[cmd][1]
    nsi = si + move_dict[cmd][0]
    nsj = sj + move_dict[cmd][1]
    if 0 < nki <= 8 and 0 < nkj <= 8 and 0 < nsi <= 8 and 0 < nsj <= 8:
        ki, kj, si, sj = nki, nkj, nsi, nsj
        print(cmd)
        print(ki, kj)
        print(si, sj)
        print()

print(ki, kj)
print(si, sj)
