def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def add(a, b):
    return a + b

print("Sum of 3 and 4:", add(3, 4))
print("Is 7 prime?", is_prime(7))

