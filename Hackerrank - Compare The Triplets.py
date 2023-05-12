a = list(map(int, input("Enter Alice's rates: ").rstrip().split()))
b = list(map(int, input("Enter Bob's rates: ").rstrip().split()))
if len(a) > 3 or len(b) > 3:
    print("You have entered more than three ratings")
elif max(a) > 100 or max(b) > 100:
    print("Do not enter a rate bigger that 100 !")
else:
    a_point = 0
    b_point = 0
    if a[0] > b[0]:
        a_point += 1
    elif a[0] < b[0]:
        b_point += 1
    if a[1] > b[1]:
        a_point += 1
    elif a[1] < b[1]:
        b_point += 1
    if a[2] > b[2]:
        a_point += 1
    elif a[2] < b[2]:
        b_point += 1
    print(f'Alice = {a_point}', end=f'  Bob = {b_point}')