def facto(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def piCal(n):
    for i in range(n):
        print(12 * (((-1)**i*facto(6*i)*(13591409+545140134*i) /
              (facto(3*i) * (facto(i)**3)*(640320**(3*i+3/2))))))
    return "fin"


print(piCal(10))
