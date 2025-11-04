def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print(i)
