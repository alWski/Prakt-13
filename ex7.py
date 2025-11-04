import math

def common_multiples(a, b, n):
    lcm = math.lcm(a, b)
    for i in range(1, n // lcm + 1):
        multiple = lcm * i
        if multiple <= n:
            print(multiple)
