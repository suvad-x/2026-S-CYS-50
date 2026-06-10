def main():
    try:
        user_input = input("Enter your number: ")
        num = int(user_input)
        print(num)
    except ValueError:
        print("Invalid")
    finally:
        print("Hello World")

if __name__ == "__main__":
    main()