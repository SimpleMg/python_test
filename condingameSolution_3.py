
variable_name = input()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
v = []
for i in variable_name:
    v.append(i)
cpt = 0
while "_" in v:
    if v[cpt] == "_":
        if cpt+1 <= len(v) - 1:
            v[cpt+1] = v[cpt+1].upper()
        del v[cpt]
    cpt += 1
print("".join(v))
