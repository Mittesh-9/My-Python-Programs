# Fibonacci Sequence

# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)
# Output hume chahiye 0 1 1 2 3 5 8 13 21 34 55 ...

# f(n) = f(n-1) + f(n-2)

def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)


def fibo(start, end):
    sequence = []
    for n in range(start, end + 1):
        sequence.append(f(n))
    return sequence


print(fibo(0, 10))