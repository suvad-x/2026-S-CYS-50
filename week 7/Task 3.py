n = 4
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    for s in range(spaces):
        print(" ", end="\t")
    for k in range(stars):
        print("*", end="\t")
    print()
for i in range(n - 1, 0, -1):
    spaces = n - i
    stars = 2 * i - 1
    for s in range(spaces):
        print(" ", end="\t")
    for k in range(stars):
        print("*", end="\t")
    print()