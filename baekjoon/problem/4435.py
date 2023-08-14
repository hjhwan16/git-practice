# 중간계 전쟁 / 20230814

T = int(input())

for tc in range(1, T+1):
    gandalph = list(map(int,input().split()))
    sauron = list(map(int, input().split()))

    gan = [1, 2, 3, 3, 4, 10]
    sau = [1, 2, 2, 2, 3, 5, 10]

    gan_score = 0
    sau_score = 0

    for i in range(len(gandalph)):
        gan_score += gan[i] * gandalph[i]

    for i in range(len(sauron)):
        sau_score += sau[i] * sauron[i]

    if gan_score > sau_score:
        print(f"Battle {tc}: Good triumphs over Evil")
    elif sau_score > gan_score:
        print(f"Battle {tc}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {tc}: No victor on this battle field")
