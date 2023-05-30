a = [4, 5, 6, 7, 8, 9, 10]
k = 2
queries = [1, 2]


def circularArrayRotation(a: list, k: int, queries: list):

    for i in range(k):
        num = a[-1]
        a.pop(-1)
        a.insert(0, num)
    res = []
    for x in queries:
        res.append(a[x])
    return res


print(circularArrayRotation(a, k, queries))
