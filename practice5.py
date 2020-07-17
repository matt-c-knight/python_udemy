temps = [221, 345, 356, -9999, 230]
# if doing if/else, for loop goes at very end
new_temps = [temp / 10 for temp in temps if temp != -9999]
newer_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)
print(newer_temps)

def mean(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(mean("matt", "josh", "cinthia", "david"))


