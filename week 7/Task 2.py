n = 4
for i in range(1, n + 1):
    spaces = n - i
    for j in range(spaces):
        print(" ", end="\t")
    stars = (i * 2) - 1
    for k in range(stars):
        print("*", end="\t")
    print()