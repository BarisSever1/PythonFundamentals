count = int(input("How many socks are there? "))
while True:
    color_list = list(map(int, input("Enter the socks colors: ").rstrip().split()))
    if len(color_list) != count:
        print("You have entered wrong number of socks, please enter again.")
        continue
    else:
        arr = []
        for i in set(color_list):
            ct = 0
            for a in color_list:
                if a == i:
                    ct += 1
            arr.append(ct)
        break

result = 0
for i in arr:
   result += ((i - (i % 2)) / 2)
print(f'There are {result} pair of socks.')