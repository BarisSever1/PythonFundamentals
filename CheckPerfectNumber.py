number = int(input("Enter the number: "))
sumar = 0
dividends = []
for i in range(1, number):
    if number % i == 0:
        dividends.append(i)
for i in range(0, len(dividends)):
    sumar = sumar + dividends[i]
if sumar == number:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")