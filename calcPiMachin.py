from numpy import arctan


def suite_fibonnacci(n: int) -> list[int]:
    suite_fibo = []
    for i in range(n + 1):
        if i == 0:
            suite_fibo.append(0)
        elif i == 1:
            suite_fibo.append(1)
        else:
            suite_fibo.append(suite_fibo[i - 1] + suite_fibo[i - 2])
    return suite_fibo[3::]


def calcPi(n: int):
    d = suite_fibonnacci(n)
    for i in range(0, len(d), 2):
        print(4 * arctan(1/d[i]))
    print(4 * arctan(1/d[-1]))


calcPi(100)
