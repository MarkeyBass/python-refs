def factorial(n: int) -> int:
    """
    returns the factorial of n
    :param n: a positive int (0 or greater)
    :return: the factorial of n
    """
    # n must be an int
    # n must be 0 or greater

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


print("MAIN start")
factorial(2.5)
print("MAIN end")
