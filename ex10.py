def print_numbers(A, B):
    if A > B:
        A, B = B, A
    allowed_digits = {'1', '3', '4', '8', '9'}
    
    for num in range(A, B + 1):
        digits = set(str(num))
        
        if digits.issubset(allowed_digits):
            print(num)
