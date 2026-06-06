def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def c_to_f(celsius):
    return (celsius * 9 / 5) + 32
choice = input("Convert F to C or C to F? (fc/cf): ").lower()
if choice == "fc":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", round(f_to_c(f), 2))
elif choice == "cf":
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", round(c_to_f(c), 2))
else:
    print("Invalid choice!")