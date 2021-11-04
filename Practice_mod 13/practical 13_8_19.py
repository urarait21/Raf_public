price = 0

n = int(input('Введите число билетов:'))

i = 1
while i <= n:
    age = int(input('Введите возраст для билета ' + str(i) + ':'))
    i = i + 1

    if (age >= 18 and age < 25):
        price = price + 990
    elif (age >= 25):
        price = price + 1390
    continue
if (n > 3):
    price = price - (price / 10)

print('Стоимость билетов:', price)