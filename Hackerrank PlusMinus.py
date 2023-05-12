arr = list(map(int, input("Enter numbers: ").rstrip().split()))
plus = 0
minus = 0
neutral = 0
for i in arr:
    if i > 0:
        plus += 1
    elif i < 0:
        minus += 1
    else:
        neutral += 1
print(f' Positiv =  {float(plus / len(arr))}')
print(f' Negativ =  {float(minus / len(arr))}')
print(f' Neutral =  {float(neutral / len(arr))}')