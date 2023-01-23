def suite_fibo_rec(n:int)->int:
    if n == 1:
        return 1
    else:
        return n + suite_fibo_rec(n - 1)


print(suite_fibo_rec(10))
