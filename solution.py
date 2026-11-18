def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('nonnegative integer required')
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def solve(value):
    return fibonacci(value)
