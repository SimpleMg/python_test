x = input()
def list_to_dict(li):
    dct = {li[i]: li[i + 1] for i in range(0, len(li), 2)}
    return dct
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
v = []
for i in x:
    v.append(i)
    v.append(0)
appears = list_to_dict(v)
for i in range(len(v) - 1):
    if v[i] in appears:
        appears[v[i]] += 1
        if appears[v[i]] > 1:
            v[i] += (v[i] * (appears[v[i]] - 1))
v = list(filter(lambda a: a != 0, v))
print("".join(v))
