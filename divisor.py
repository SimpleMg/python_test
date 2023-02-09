def divisieur(number:int)->list[int]:
    divisor = 1
    list_of_divisor = []
    while divisor != number + 1:
        if number % divisor == 0:
            list_of_divisor.append(divisor)
        divisor += 1
    return list_of_divisor
print(divisieur(24))
