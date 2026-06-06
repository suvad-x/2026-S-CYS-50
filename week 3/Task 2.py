large = lambda a, b: a if a > b else b
def print_table(num, upto):
    print("Multiplication Table of", num, "up to", upto)
    for i in range(1, upto + 1):
        print(num, "x", i, "=", num * i)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
largest = large(a, b)
print("Largest number is:", largest)
range_upto = int(input("Enter range for table: "))
print_table(largest, range_upto)