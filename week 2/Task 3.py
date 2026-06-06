start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
primes = []
total = 0
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            total += num
print("Prime numbers:", primes)
print("Sum of primes:", total)