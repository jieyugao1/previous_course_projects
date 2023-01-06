def gcd(a, b):
    assert int(a) == a and int(b) == b, "Both numbers should be integers!"
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a 
    return gcd(b, a%b)
print(gcd(48,18))
print(gcd(48, -18))

