# Quiz 1: Prime Numbers in a Range

# Write a function prime_in_range(start, end)
# that returns a list of all
# prime numbers between start and end (inclusive).

def prime_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num <= 1:
            print(f"{num} is not a prime number.")
        else:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# Input from user
start = int(input("Enter the first number of the range: "))
end = int(input("Enter the second number of the range: "))

print("Prime numbers in range:", prime_in_range(start, end))