def factorial(n: int) -> int:
    """
    returns the factorial of n.

    n must be an int (TypeError is raised)
    n must be a value of 0 or greater (ValueError is raised)

    :param n: a positive int (0 or greater)
    :return: the factorial of n
    """

    if type(n) is not int:
        raise TypeError("n must be an int")

    if n < 0:
        raise ValueError("n must be 0 or greater")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


print("MAIN start")
print(factorial(-11))
print("MAIN end")
