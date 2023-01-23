def puissance(a:int, n:int)->int:
    if n == 0:
        return 1
    else:
        return a * puissance(a, n - 1)


print(puissance(3, 3))
