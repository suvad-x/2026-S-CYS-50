bytes_value = float(input("Enter bytes: "))

mb = bytes_value / (1024 * 1024)
gb = bytes_value / (1024 * 1024 * 1024)

print("Mega Bytes =", mb)
print("Giga Bytes =", gb)