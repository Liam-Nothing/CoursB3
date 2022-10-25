def puissance(x, n):
    if n == 0:
        return 1
    return puissance(x, n-1)*x

print(puissance(2, 10))