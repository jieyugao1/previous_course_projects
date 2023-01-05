
def sumofDigits(n):
    assert n >= 0 and int(n) == n, "n should be an positive integer"
    if n < 10:
        return n
    else:
        return n%10 + sumofDigits(n//10)
print(sumofDigits(20))
print(sumofDigits(1019))
print(sumofDigits(-10))
