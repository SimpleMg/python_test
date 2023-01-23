def factorielle_rec(n:int)->int:
    if n == 1:
        return 1
    else:
        return n * factorielle_rec(n - 1)


print(factorielle_rec(10))
