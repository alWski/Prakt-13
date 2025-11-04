def print_fibonacci(n):
    if n <= 0:
        return
    fib1, fib2 = 1, 1
    if n >= 1:
        print(fib1, end=" ")
    if n >= 2:
        print(fib2, end=" ")
    for i in range(2, n):
        fib_next = fib1 + fib2
        print(fib_next, end=" ")
        fib1, fib2 = fib2, fib_next

n = int(input())
print_fibonacci(n)
