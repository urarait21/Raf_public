per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

money = int(input('Введите депозит:'))

tkb = per_cent.get('ТКБ')
skb = per_cent.get('СКБ')
vtb = per_cent.get('ВТБ')
sber = per_cent.get('СБЕР')

deposit.append((tkb * money)/100)
deposit.append((skb * money)/100)
deposit.append((vtb * money)/100)
deposit.append((sber * money)/100)

print(deposit)

max_number = max(deposit)
print("Максимальная сумма по депозиту:", max_number)