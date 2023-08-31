n = int(input())

def function(n):
    if int(n**(1/2)) == n**(1/2):
        return 1

    for i in range(1, int(n**(1/2))+1):
        if int((n - i**2)**(1/2)) == (n - i**2)**(1/2):
            return 2

    for i in range(1, int(n**(1/2))+1):
        for j in range(1, int((n - i**2)**(1/2))+1):
            if int((n - i ** 2 - j ** 2) ** (1 / 2)) == (n - i ** 2 - j**2) ** (1 / 2):
                return 3
    return 4

print(function(n))

