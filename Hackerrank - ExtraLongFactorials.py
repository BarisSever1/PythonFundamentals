n = 25


def extra_long_factorials(n):
    ct = 0
    res = 1
    while n > ct:
        res = res * (n - ct)
        ct += 1
    return res


print(extra_long_factorials(n))
