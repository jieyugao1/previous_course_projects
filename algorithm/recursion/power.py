def power(n, a):
    # return n**a
    assert int(a) == a, "the exponent must be an integer!"
    while a > 0:
        return n * power(n, a-1)
    while a < 0:
        return 1/n * power(n, a + 1)
    return 1
print(power(2, 8))
print(power(-2, -7))
print(power(2.1, 3))
