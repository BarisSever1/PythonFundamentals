
n = 5
m = 2
s = 2


def saveThePrisoner(n, m, s):
    ct = s
    candy = m
    while candy > 0:
        candy -= 1
        if candy == 0:
            break
        if ct == n:
            ct = 1
        else:
            ct += 1
    print(ct)


saveThePrisoner(n, m, s)
