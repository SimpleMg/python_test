n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


if n % 2 != 0:
    print((n // 2) * n)
else:
    print((n // 2) * (n-1))
