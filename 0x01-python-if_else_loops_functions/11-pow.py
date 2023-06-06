def pow(a, b):
    """
    Computes a to the power of b and returns the value.
    """
    result = 1

    for _ in range(b):
        result *= a

    return result


print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

