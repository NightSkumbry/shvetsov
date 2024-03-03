
a = range(59, 228)
# a = range(228, 1000)

for x in range(1000):
    k = ((x in range(59, 229)) <= (x in a)) or (((x%3 == 0) <= (x in range(257, 357))) <= ((x in range(5, 601)) <= (x in a)))
    if not k:
        print(x)
print(len(a))











