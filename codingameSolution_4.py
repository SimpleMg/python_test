n = int(input())
text = input()
cpt = 0
for i in range(len(text) - 1):
    for j in range(cpt, n):
        print(text[j], end="")
    print()
    cpt += 1
    n+= 1
    if n-1 == len(text):
        break
