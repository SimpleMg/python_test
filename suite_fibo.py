def suite_fibonnacci(n: int)-> list[int]:
    suite_fibo = []
    for i in range(n + 1):
        if i == 0:
            suite_fibo.append(0)
        elif i == 1:
            suite_fibo.append(1)
        else:
            suite_fibo.append(suite_fibo[i - 1] + suite_fibo[i - 2])
    return suite_fibo


f = suite_fibonnacci(10)
for i in range(len(f)):
    print("F {} = {}".format(i, f[i]))
