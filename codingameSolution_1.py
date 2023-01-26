s = input()

s = s.split()
if (len(s)) % 2 == 0:
    print("".join([s[(int(len(s)/2)) - 1], s[(int(len(s)/2))]]))
else:
    print(s[(int(len(s)/2))])
